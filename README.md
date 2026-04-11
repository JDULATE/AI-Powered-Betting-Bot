# Betting Bot — AI-Powered Parlay Analysis

Quantitative sports betting analysis system focused on elite football.
Uses Gemini API (free tier) to generate statistical analysis, Poisson modeling,
Monte Carlo simulation, and optimized parlay construction for DoradoBet.

---

## 📁 Project Structure

```
betting-bot/
├── config.py          ← EDIT DAILY (bankroll, date, matches)
├── analyzer.py        ← Analysis engine (do not edit)
├── main.py            ← Entry point — run this every day
├── .env               ← API keys (never commit to git)
├── .gitignore         ← Protects your .env
├── logs/              ← Analysis history
└── outputs/           ← Generated reports
```

---

## ⚙️ Installation

### 1. Requirements
- Python 3.8 or higher
- pip

### 2. Create project folder

```bash
mkdir betting-bot
cd betting-bot
```

### 3. Install dependencies

```bash
pip install google-genai python-dotenv requests
```

### 4. Get your free Gemini API key

1. Go to [aistudio.google.com/apikey](https://aistudio.google.com/apikey)
2. Sign in with your Google account
3. Click **"Create API key"** → **"Create API key in new project"**
4. Copy the generated key

### 5. Configure the `.env` file

Create a `.env` file in the project root:

```env
GEMINI_API_KEY=AIzaSy_xxxxxxxxxxxxxxxxxxxxxxxx
```

### 6. Create `.gitignore`

```bash
echo ".env" >> .gitignore
echo "outputs/" >> .gitignore
echo "logs/" >> .gitignore
echo "__pycache__/" >> .gitignore
```

---

## 🚀 Daily Usage

### Step 1 — Update bankroll in `config.py`

```python
BANCA_ACTUAL = 5000   # ← update this every day
```

### Step 2 — Optional: specify matches

```python
PARTIDOS_ESPECIFICOS = [
    "Real Madrid vs Barcelona",
    "Liverpool vs Arsenal",
]
# Leave empty [] for automatic search
```

### Step 3 — Run the analysis

```bash
python main.py
```

### Step 4 — Read the report

The report is printed to the console and automatically saved in `outputs/`.

---

## 📊 Bankroll Ladder Stages

| Stage | Bankroll | Target Odds | Stake | Picks |
|-------|----------|-------------|-------|-------|
| 0 | < ₡20,000 | 1.80 | 30% | 2 |
| 1 | ₡20,000 – ₡79,999 | 2.00 | 40% | 2 |
| 2 | ₡80,000 – ₡199,999 | 1.90 | 40% | 2 |
| 3 | ₡200,000 – ₡499,999 | 1.85 | 30% | 2 |
| 4 | ≥ ₡500,000 | 1.77 | 20% | 2 |

Stage is **automatically detected** based on the bankroll set in `config.py`.

---

## 🏆 Leagues Covered

**Core (highest priority)**
- UEFA Champions League / Europa League
- Premier League, La Liga, Serie A
- Bundesliga, Ligue 1
- English Championship, Eredivisie

**Secondary (only if statistically superior)**
- UEFA Conference League
- Liga Promerica / Copa Costa Rica
- UEFA Qualifiers

---

## 🔍 Analysis Methodology

Each run executes 10 phases:

1. **Match filter** — discards matches with insufficient data
2. **Data collection** — recent form, xG, squad context
3. **Statistical modeling** — adjusted attack/defense ratings
4. **Poisson distribution** — market probabilities per match
5. **Monte Carlo simulation** — 10,000 simulated matches per game
6. **Value bet detection** — EV = (real_prob × odds) − 1
7. **Safety filter** — only picks with probability ≥ 72%
8. **Market hierarchy** — Over 1.5 → Under 4.5 → etc.
9. **Parlay construction** — optimal combination
10. **Quality control** — final consistency check

---

## 📝 Report Format

Every analysis generates a full report with:

- Day summary and detected bankroll stage
- Detailed analysis of top candidate matches
- Top 5 picks of the day
- **Main recommended parlay** with stake in ₡
- Conservative alternative parlay
- Best single pick of the day
- Final conclusion and betting recommendation

---

## 🛠️ Troubleshooting

**Error: `GEMINI_API_KEY not found`**
→ Check that the `.env` file exists and contains the correct key

**Error: `ModuleNotFoundError`**
→ Run `pip install google-genai python-dotenv requests`

**Error: `429 RESOURCE_EXHAUSTED`**
→ The model is temporarily rate-limited. Wait 30 seconds and try again.
→ Or switch model in `analyzer.py` to `gemini-2.5-flash-lite`

**Pylance warning: `Import could not be resolved`**
→ This is a VS Code display issue only — the code runs fine.
→ Fix: `Ctrl+Shift+P` → "Python: Select Interpreter" → select Python 3.11

**Report is too short or incomplete**
→ Change model in `analyzer.py` to `gemini-2.5-pro` for deeper analysis

**Matches not from today**
→ Gemini uses internal knowledge. For real-time data, manually specify
  matches in `PARTIDOS_ESPECIFICOS` inside `config.py`

---

## ⚠️ Disclaimer

- This system is an analysis tool — **it does not guarantee results**
- Never bet more than the recommended stake for your current stage
- If the analysis recommends not betting that day, respect that recommendation
- Always read the full report before making any decisions
- Sports betting involves real risk of financial loss

---

## 📈 Future Roadmap

- [ ] API-Football integration for real-time match data
- [ ] Web dashboard to visualize analysis history
- [ ] Automatic result tracking vs predictions
- [ ] Telegram alerts when a strong parlay is available

---

*Mode: Ultra Conservative — Goal: ₡500,000*
