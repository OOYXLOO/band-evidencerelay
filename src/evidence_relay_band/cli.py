from __future__ import annotations

import argparse
import http.server
import socketserver
from pathlib import Path

from evidence_relay_band.render import render_html
from evidence_relay_band.render import render_submission_summary
from evidence_relay_band.simulator import simulate_room
from evidence_relay_band.simulator import write_transcript


def generate(args: argparse.Namespace) -> None:
    transcript = simulate_room(Path(args.evidencelock_root).resolve())
    out_dir = Path(args.out).resolve()
    transcript_path = write_transcript(transcript, out_dir)
    html_path = render_html(transcript, out_dir)
    summary_path = render_submission_summary(transcript, out_dir)
    print(f"Wrote {transcript_path}")
    print(f"Wrote {html_path}")
    print(f"Wrote {summary_path}")


def serve(args: argparse.Namespace) -> None:
    directory = Path(args.directory).resolve()
    handler = lambda *handler_args, **handler_kwargs: http.server.SimpleHTTPRequestHandler(
        *handler_args,
        directory=str(directory),
        **handler_kwargs,
    )
    with socketserver.TCPServer((args.host, args.port), handler) as server:
        print(f"Serving {directory} at http://{args.host}:{args.port}/")
        server.serve_forever()


def main() -> None:
    parser = argparse.ArgumentParser(description="EvidenceRelay Band helper.")
    sub = parser.add_subparsers(required=True)
    gen = sub.add_parser("generate")
    gen.add_argument("--evidencelock-root", required=True)
    gen.add_argument("--out", default="build")
    gen.set_defaults(func=generate)

    srv = sub.add_parser("serve")
    srv.add_argument("--directory", default="build")
    srv.add_argument("--host", default="127.0.0.1")
    srv.add_argument("--port", type=int, default=8765)
    srv.set_defaults(func=serve)

    args = parser.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()
