from modules.vision import Vision
import cv2


eyes = Vision()

SPACING = "41cm"


TRIAL = ["1","2","3"]

DISTANCE = [
    "30cm",
    "60cm",
    "90cm",
    "120cm",
    "150cm",
    "180cm",
    "210cm",
    "240cm",
    "270cm",
    "300cm",
]

for d in DISTANCE:

    while True:

        k = cv2.waitKey(10)

        print(f"Press s to capture calibration image {d}.")

        onion = eyes.onion_array(lowres=False)
        joined = eyes.joined_array(lowres=False)

        scaled_down = onion[::4, ::4]

        cv2.imshow("Calibration Feed", scaled_down)

        if k == 115:  # s
            break

    cv2.imwrite(f"images/{SPACING}/dist_{d}_calibration.png", joined)
    print("READY ----------------------------------------------")

cv2.destroyAllWindows()


for t in TRIAL:
    for d in DISTANCE:

        while True:

            joined = eyes.joined_array(lowres=False)

            scaled_down = joined[::6, ::6]

            cv2.imshow("Feed", scaled_down)

            k = cv2.waitKey(10)

            print(f"Trial {t}, Distance {d}.")

            if k == 32:  # space
                break

        cv2.imwrite(f"images/{SPACING}/dist_{d}_take_{t}.png", joined)
        print("READY ----------------------------------------------")

cv2.destroyAllWindows()
