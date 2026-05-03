import re
with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

# Revert theme color
text = text.replace('<meta name="theme-color" content="#7c1d1d" />', '<meta name="theme-color" content="#4c1d95" />')

# Revert CSS variables and .card
text = re.sub(r':root\s*\{.*?\.card:active\s*\{.*?\}', ''':root {
      --brand: #4c1d95;
      --brand-2: #7c3aed;
      --gold: #f59e0b;
      --ink: #0f172a;
      --bg: #f8fafc;
    }

    html,
    body {
      height: 100%;
    }

    body {
      font-family: 'Inter', ui-sans-serif, system-ui, -apple-system, sans-serif;
      background: var(--bg);
      color: var(--ink);
      overflow-x: hidden;
      -webkit-tap-highlight-color: transparent;
    }

    .brand-grad {
      background: linear-gradient(135deg, var(--brand) 0%, var(--brand-2) 100%);
    }

    .card {
      background: #fff;
      border-radius: 20px;
      box-shadow: 0 2px 8px rgba(0, 0, 0, .04), 0 8px 24px rgba(0, 0, 0, .06);
      transition: transform 0.2s ease, box-shadow 0.2s ease;
    }''', text, flags=re.DOTALL)

# Footer removal (this replaces the exact string or regex for the footer)
text = re.sub(r'<!-- FOOTER pinned to bottom -->.*?</div>', '<!-- FOOTER pinned to bottom -->\n    <div style="margin-top:auto;"></div>', text, flags=re.DOTALL)

# Revert hardcoded red/amber/rose colors to purple
text = text.replace('from-red-50 to-amber-50', 'from-purple-50 to-indigo-50')
text = text.replace('bg-red-50 rounded-full', 'bg-purple-50 rounded-full')
text = text.replace('bg-rose-50 border border-rose-100 flex items-center justify-center text-rose-700', 'bg-purple-50 border border-purple-100 flex items-center justify-center text-purple-700')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(text)
