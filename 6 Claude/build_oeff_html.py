# ── Build ─────────────────────────────────────────────────────────────────────
def build(predictions_path: str, results_path: str, out_path: str) -> None:
    players       = load_predictions(predictions_path)
    model_results = load_model_results(results_path)

    players_json = json.dumps(players,       ensure_ascii=False)
    results_json = json.dumps(model_results, ensure_ascii=False)

    html = HTML_TEMPLATE.replace('"%%PLAYERS_DATA%%"',       players_json)
    html = html.replace('"%%MODEL_RESULTS_DATA%%"', results_json)

    with open(out_path, "w", encoding="utf-8") as f:
        f.write(html)

    print(f"\n  Output: {out_path}", file=sys.stderr)
    print(f"  Players: {len(players)}", file=sys.stderr)
    print(f"  Model runs: {len(model_results)}", file=sys.stderr)
    print(f"  File size: {len(html)//1024} KB", file=sys.stderr)


# ── CLI ───────────────────────────────────────────────────────────────────────
if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Bake OEFF pipeline CSVs into a self-contained HTML explorer."
    )
    parser.add_argument("--predictions", default="player_predictions.csv",
                        help="Path to player_predictions.csv (default: player_predictions.csv)")
    parser.add_argument("--results",     default="oeff_model_results_2021_2025.csv",
                        help="Path to model results CSV (default: oeff_model_results_2021_2025.csv)")
    parser.add_argument("--out",         default="oeff_explorer.html",
                        help="Output HTML file (default: oeff_explorer.html)")
    args = parser.parse_args()

    build(args.predictions, args.results, args.out)
    print(f"\nDone! Open {args.out} in any browser.")