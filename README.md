<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0"/>
  <title>Majix Discord Spammer Tool</title>
  <style>
    body {
      font-family: Arial, sans-serif;
      background: #f7f7f7;
      color: #333;
      max-width: 800px;
      margin: auto;
      padding: 2rem;
      line-height: 1.6;
    }
    h1, h2, h3 {
      color: #222;
    }
    code {
      background-color: #eee;
      padding: 2px 6px;
      border-radius: 4px;
      font-family: monospace;
    }
    pre {
      background: #eee;
      padding: 1rem;
      border-radius: 6px;
      overflow-x: auto;
    }
    .warning {
      color: red;
      font-weight: bold;
    }
    a {
      color: #0066cc;
    }
  </style>
</head>
<body>

  <h1>📄 Majix Discord Spammer Tool</h1>

  <h3>🔧 Created by: <strong>MaJiX</strong></h3>

  <h2>💬 Description</h2>
  <p>This tool allows you to send automated repeated messages to one or more Discord channels using your <strong>user token</strong>.<br/>
  <em>For personal testing or educational use only.</em></p>

  <h2>🚀 How to Run</h2>
  <h3>✅ Requirements:</h3>
  <ol>
    <li>Install Python<br/>
      <a href="https://www.python.org/downloads/" target="_blank">Download from python.org</a><br/>
      ✅ Be sure to check <strong>"Add Python to PATH"</strong> during installation.
    </li>
    <li>Install the required library:
      <pre><code>pip install discum</code></pre>
    </li>
  </ol>

  <h2>🖥 How to Use</h2>
  <ol>
    <li>Run the script using Python:
      <pre><code>python discord_spammer.py</code></pre>
    </li>
    <li>Follow the prompts:
      <ul>
        <li>Enter your <strong>Discord token</strong></li>
        <li>Enter one or more <strong>channel IDs</strong>, separated by commas</li>
        <li>Enter the <strong>message</strong> you want to send</li>
      </ul>
    </li>
    <li>Control the spammer using these commands:
      <ul>
        <li><code>s</code> — Start sending messages</li>
        <li><code>p</code> — Pause sending messages</li>
        <li><code>q</code> — Quit the program</li>
      </ul>
    </li>
  </ol>

  <h2>🔐 How to Find Your Discord Token</h2>
  <p class="warning">⚠️ WARNING: Your token gives full access to your account. Never share it.</p>
  <ol>
    <li>Open Discord in a <strong>browser</strong> (not the app).</li>
    <li>Press <code>Ctrl + Shift + I</code> to open Developer Tools.</li>
    <li>Go to the <strong>Application</strong> tab.</li>
    <li>Under <strong>Storage</strong>, click <strong>Local Storage</strong>.</li>
    <li>Select <code>https://discord.com</code>.</li>
    <li>Search for the key named <code>token</code> — your user token will be shown on the right.</li>
  </ol>

  <h2>🧠 Disclaimer</h2>
  <p>This tool is provided <strong>for educational purposes only</strong>.<br/>
  Misuse may violate Discord’s <a href="https://discord.com/terms" target="_blank">Terms of Service</a> and result in account suspension or ban.<br/>
  <strong>Use responsibly and at your own risk.</strong></p>

</body>
</html>
