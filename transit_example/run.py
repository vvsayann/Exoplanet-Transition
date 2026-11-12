from pathlib import Path
import allesfitter
def main():
    data_dir = Path(__file__).resolve().parent / "allesfit"
    figures = allesfitter.show_initial_guess(
        str(data_dir), do_logprint=False, return_figs=True
    )
    plot_path = data_dir / "results" / "initial_guess_b.png"
    figures[0].savefig(plot_path, dpi=150, bbox_inches="tight")
    print(f"Initial transit model saved to {plot_path}")
if __name__ == "__main__":
    main()
