
from datetime import datetime
from pathlib import Path
from typing import List, Dict

def generate_report(target: str, open_ports: List[Dict], output_dir: str = "reports") -> str:
    """
    Generate a simple HTML report for PortBlitz v1.0.
    """
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    filename = f"{target}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.html"
    out_path = Path(output_dir) / filename
    
    # Ensure reports dir exists
    out_path.parent.mkdir(exist_ok=True)

    rows = ""
    for p in open_ports:
        rows += f"""
        <tr>
            <td>{p['port']}</td>
            <td>TCP</td>
            <td><span class="badge open">OPEN</span></td>
            <td>{p.get('service', 'Unknown')}</td>
        </tr>
        """

    html = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>PortBlitz Report - {target}</title>
        <style>
            :root {{
                --bg: #0f172a;
                --card: #1e293b;
                --text: #f8fafc;
                --accent: #38bdf8;
                --success: #22c55e;
            }}
            body {{
                font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
                background-color: var(--bg);
                color: var(--text);
                margin: 0;
                padding: 2rem;
            }}
            .container {{
                max-width: 900px;
                margin: 0 auto;
            }}
            .header {{
                text-align: center;
                margin-bottom: 3rem;
                padding: 2rem;
                background: var(--card);
                border-radius: 12px;
                box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.5);
                border: 1px solid #334155;
            }}
            h1 {{ margin: 0; color: var(--accent); }}
            .meta {{ color: #94a3b8; margin-top: 0.5rem; }}
            
            table {{
                width: 100%;
                border-collapse: collapse;
                background: var(--card);
                border-radius: 8px;
                overflow: hidden;
            }}
            th, td {{
                padding: 1rem;
                text-align: left;
                border-bottom: 1px solid #334155;
            }}
            th {{
                background: #0f172a;
                color: var(--accent);
                font-weight: 600;
                text-transform: uppercase;
                letter-spacing: 0.05em;
            }}
            tr:hover {{ background: #263346; }}
            
            .badge {{
                padding: 0.25rem 0.75rem;
                border-radius: 9999px;
                font-size: 0.875rem;
                font-weight: 500;
            }}
            .open {{ background: rgba(34, 197, 94, 0.2); color: var(--success); text-align: center; display: inline-block; }}
            
            .footer {{
                text-align: center;
                margin-top: 3rem;
                color: #64748b;
                font-size: 0.9rem;
            }}
            .branding {{ color: var(--accent); font-weight: bold; }}
        </style>
    </head>
    <body>
        <div class="container">
            <div class="header">
                <h1>⚡ PortBlitz Report</h1>
                <div class="meta">Target: <strong>{target}</strong> | Scan Time: {timestamp}</div>
            </div>

            <table>
                <thead>
                    <tr>
                        <th>Port</th>
                        <th>Protocol</th>
                        <th>Status</th>
                        <th>Service (Guess)</th>
                    </tr>
                </thead>
                <tbody>
                    {rows}
                </tbody>
            </table>

            <div class="footer">
                Built By <span class="branding">MIHx0</span> (Mizaz Haider) • Powered By <span class="branding">The PenTrix</span>
            </div>
        </div>
    </body>
    </html>
    """
    
    out_path.write_text(html, encoding="utf-8")
    return str(out_path)
