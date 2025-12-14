import * as vscode from "vscode";

export function activate(context: vscode.ExtensionContext) {
  const disposable = vscode.commands.registerCommand(
    "hybrid.run",
    async () => {
      const editor = vscode.window.activeTextEditor;
      if (!editor) {
        vscode.window.showErrorMessage("No active editor");
        return;
      }

      // 1️⃣ Read selected text or current line
      const selection = editor.selection;
      const prompt = selection.isEmpty
        ? editor.document.lineAt(selection.active.line).text
        : editor.document.getText(selection);

      if (!prompt.trim()) {
        vscode.window.showWarningMessage("No input text found");
        return;
      }

      vscode.window.showInformationMessage("🧠 Hybrid AI thinking...");

      try {
        // 2️⃣ Call FastAPI backend
        const response = await fetch("http://127.0.0.1:8000/generate", {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
          },
          body: JSON.stringify({
            prompt: prompt,
            generate_tests: false, // 🔒 NO TESTS BY DEFAULT
          }),
        });

        if (!response.ok) {
          throw new Error(`Backend error: ${response.status}`);
        }

        const data = await response.json();

        // 3️⃣ Safe parsing
        const code: string =
          typeof data.code === "string" ? data.code : "";

        const accuracy: number =
          typeof data.accuracy === "number" ? data.accuracy : 0;

        if (!code.trim()) {
          vscode.window.showWarningMessage("AI returned no code");
          return;
        }

        // 4️⃣ Insert ONLY code
        await editor.edit((editBuilder) => {
          editBuilder.insert(
            editor.selection.active,
            `

# === AI Generated Code ===
${code}
`
          );
        });

        // 5️⃣ Accuracy popup
        vscode.window.showInformationMessage(
          `✅ AI Accuracy Score: ${accuracy}%`
        );

      } catch (err: any) {
        vscode.window.showErrorMessage(
          `❌ Hybrid AI failed: ${err.message}`
        );
      }
    }
  );

  context.subscriptions.push(disposable);
}

export function deactivate() {}
