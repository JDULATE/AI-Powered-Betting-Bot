# Betting Bot — AI-Powered Parlay Analysis

Quantitative sports betting analysis system focused on elite football.
Uses Gemini API (free tier) + API-Football (free tier) to fetch real today's matches,
generate statistical analysis, Poisson modeling, Monte Carlo simulation,
and optimized parlay construction for DoradoBet.

---

## 📁 Project Structure

```
betting-bot/
├── config.py          ← EDIT DAILY (bankroll only — matches are automatic)
├── data_fetcher.py    ← Fetches real today's matches from API-Football
├── analyzer.py        ← Analysis engine powered by Gemini AI
├── main.py            ← Entry point — run this every day
├── .env               ← API keys
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

### 5. Get your free API-Football key

1. Go to [dashboard.api-football.com](https://dashboard.api-football.com)
2. Sign up — no credit card required
3. Confirm your email
4. Copy the API key from your dashboard

### 6. Configure the `.env` file

Create a `.env` file in the project root:

```env
GEMINI_API_KEY=AIzaSy_xxxxxxxxxxxxxxxxxxxxxxxx
API_FOOTBALL_KEY=your_api_football_key_here
```

> ⚠️ Variable names are case-sensitive. Use exactly `GEMINI_API_KEY` and `API_FOOTBALL_KEY`.

### 7. Create `.gitignore`

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
BANCA_ACTUAL = 5000   # ← update this every day with your real bankroll
```

That's it. Matches are fetched automatically — no need to enter them manually.

### Step 2 — Run the analysis

```bash
python main.py
```

### Step 3 — Read the report

The bot will:
1. Fetch all real today's matches from API-Football
2. Filter matches from core leagues only
3. Send them to Gemini for full quantitative analysis
4. Print the complete report to console
5. Save the report automatically in `outputs/`

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
- UEFA Champions League (ID: 2)
- UEFA Europa League (ID: 3)
- Premier League (ID: 39)
- La Liga (ID: 140)
- Serie A (ID: 135)
- Bundesliga (ID: 78)
- Ligue 1 (ID: 61)
- English Championship (ID: 40)
- Eredivisie (ID: 88)

**Secondary (only if statistically superior)**
- UEFA Conference League (ID: 848)
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
- Detailed analysis of top candidate matches with xG, form, probable scores
- Top 5 picks of the day ranked by confidence
- **Main recommended parlay** with stake in ₡ and potential return
- Conservative alternative parlay
- Best single pick of the day
- Final conclusion and betting recommendation

---

## 🛠️ Troubleshooting

**`Key cargada: 'None'` / API key not loading**
→ Check variable names in `.env` — must be exactly `GEMINI_API_KEY` and `API_FOOTBALL_KEY`
→ No spaces around `=`, no quotes: `API_FOOTBALL_KEY=abc123` ✓
→ Make sure `.env` is in the same folder as `main.py`

**Error HTTP 403 on API-Football**
→ Usually means the key name in `.env` doesn't match what the code reads
→ Run `python test_api.py` to diagnose

**Error: `429 RESOURCE_EXHAUSTED` on Gemini**
→ Model temporarily rate-limited. Wait 30 seconds and retry.
→ Or switch model in `analyzer.py` to `gemini-2.5-flash-lite`

**0 matches found today**
→ API-Football free tier has a limit of 100 requests/day
→ Check remaining requests at dashboard.api-football.com
→ Or manually add matches in `config.py` under `PARTIDOS_ESPECIFICOS`

**Pylance warning: `Import could not be resolved`**
→ VS Code display issue only — code runs fine
→ Fix: `Ctrl+Shift+P` → "Python: Select Interpreter" → select Python 3.11

**Report is too short or incomplete**
→ Change model in `analyzer.py` to `gemini-2.5-pro` for deeper analysis

---

## ⚠️ Disclaimer

- This system is an analysis tool — **it does not guarantee results**
- Never bet more than the recommended stake for your current stage
- If the analysis recommends not betting that day, respect that recommendation
- Always read the full report before making any decisions
- Sports betting involves real risk of financial loss

---

## 📈 Future Roadmap

- [ ] Pull real xG and form data from API-Football for each match
- [ ] Web dashboard to visualize analysis history and track results
- [ ] Automatic result tracking vs predictions (hit rate over time)
- [ ] Telegram alerts when a strong parlay is available

---

*Mode: Ultra Conservative — Goal: ₡500,000*
