"""
MCP Server for Cutaneous High-Frequency Ultrasound (HFUS) SLEB Skill.
Provides standard Model Context Protocol JSON-RPC tool endpoints.
"""

import sys
import json
from client import HighFrequencyUltrasoundSLEBClient


def main():
    client = HighFrequencyUltrasoundSLEBClient()

    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue
        try:
            req = json.loads(line)
        except Exception:
            continue

        method = req.get("method")
        msg_id = req.get("id")

        if method == "tools/list":
            res = {
                "jsonrpc": "2.0",
                "id": msg_id,
                "result": {
                    "tools": [
                        {
                            "name": "evaluate_sleb_metrics",
                            "description": "Calculates 20-50 MHz High-Frequency Ultrasound (HFUS) Subepidermal Low-Echogenic Band (SLEB) thickness, Dermal Thickness, SLEB/Dermis ratio (SDR%), and Dermal Density Index (DDI%).",
                            "inputSchema": {
                                "type": "object",
                                "properties": {
                                    "sleb_thickness_um": {
                                        "type": "number",
                                        "description": "Subepidermal low-echogenic band thickness in micrometers (um)."
                                    },
                                    "total_dermal_thickness_mm": {
                                        "type": "number",
                                        "description": "Total dermal thickness in millimeters (mm)."
                                    },
                                    "mean_dermal_echogenicity_greyscale": {
                                        "type": "number",
                                        "description": "Mean reticular dermal echogenicity greyscale (0 - 255)."
                                    },
                                    "calibrated_max_greyscale": {
                                        "type": "number",
                                        "description": "Calibrated maximum greyscale scale (default: 255.0)."
                                    },
                                    "patient_age_years": {
                                        "type": "integer",
                                        "description": "Subject age in years (optional)."
                                    },
                                    "anatomical_site": {
                                        "type": "string",
                                        "description": "Anatomical examination site (e.g. dorsal forearm, volar forearm, cheek)."
                                    }
                                },
                                "required": [
                                    "sleb_thickness_um",
                                    "total_dermal_thickness_mm",
                                    "mean_dermal_echogenicity_greyscale"
                                ]
                            }
                        }
                    ]
                }
            }
            sys.stdout.write(json.dumps(res) + "\n")
            sys.stdout.flush()

        elif method == "tools/call":
            params = req.get("params", {})
            name = params.get("name")
            args = params.get("arguments", {})

            if name == "evaluate_sleb_metrics":
                try:
                    out = client.evaluate_sleb_metrics(**args)
                    res = {
                        "jsonrpc": "2.0",
                        "id": msg_id,
                        "result": {
                            "content": [{"type": "text", "text": json.dumps(out, indent=2)}]
                        }
                    }
                except Exception as e:
                    res = {
                        "jsonrpc": "2.0",
                        "id": msg_id,
                        "isError": True,
                        "error": {"code": -32000, "message": str(e)}
                    }
                sys.stdout.write(json.dumps(res) + "\n")
                sys.stdout.flush()


if __name__ == "__main__":
    main()
