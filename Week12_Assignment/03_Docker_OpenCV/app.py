import argparse
import json
from pathlib import Path
import cv2
import numpy as np

def process(input_path, output_path):
    if input_path:
        image = cv2.imread(str(input_path))
        if image is None:
            raise ValueError(f"Cannot read image: {input_path}")
    else:
        # Synthetic sample: three separated bright objects on a dark background.
        image = np.zeros((480, 640, 3), dtype=np.uint8)
        cv2.rectangle(image, (60, 80), (190, 210), (255, 255, 255), -1)
        cv2.circle(image, (350, 150), 65, (255, 255, 255), -1)
        cv2.rectangle(image, (240, 310), (490, 400), (255, 255, 255), -1)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)
    edges = cv2.Canny(blurred, 50, 150)
    _, mask = cv2.threshold(blurred, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    objects = [c for c in contours if cv2.contourArea(c) >= 500]
    objects.sort(key=lambda c: (cv2.boundingRect(c)[1], cv2.boundingRect(c)[0]))
    annotated = image.copy()
    measurements = []
    for i, contour in enumerate(objects, 1):
        x, y, w, h = cv2.boundingRect(contour)
        cv2.rectangle(annotated, (x, y), (x+w, y+h), (0, 255, 0), 2)
        cv2.putText(annotated, f"Object {i}", (x, max(20, y-8)),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)
        measurements.append({"id": i, "area_px": cv2.contourArea(contour),
                             "bbox": [x, y, w, h]})
    out = Path(output_path)
    out.mkdir(parents=True, exist_ok=True)
    for name, data in {"original": image, "gray": gray, "edges": edges,
                       "mask": mask, "annotated": annotated}.items():
        if not cv2.imwrite(str(out / f"{name}.png"), data):
            raise RuntimeError(f"Could not save {name}.png")
    report = {"source": str(input_path) if input_path else "synthetic_demo",
              "object_count": len(objects), "objects": measurements}
    (out / "report.json").write_text(json.dumps(report, indent=2), encoding="utf-8")
    return report

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="OpenCV object counting demo")
    parser.add_argument("--input", type=Path)
    parser.add_argument("--output", type=Path, default=Path("results"))
    args = parser.parse_args()
    print(json.dumps(process(args.input, args.output), indent=2))
