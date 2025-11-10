import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import os

TOL = 1e-10
np.set_printoptions(precision=6, suppress=True)

# create folder for saving images
os.makedirs("figures", exist_ok=True)


def classify(A):
    A = 0.5 * (A + A.T)
    eig = np.linalg.eigvalsh(A)
    if np.all(eig > TOL):
        t = "PD (Positive Definite)"
    elif np.all(eig >= -TOL) and np.any(np.abs(eig) <= TOL):
        t = "PSD (Positive Semi-Definite)"
    elif np.all(eig < -TOL):
        t = "ND (Negative Definite)"
    else:
        t = "Indefinite"
    return t, eig


def plotA(A, title, filename):
    x = np.linspace(-2.5, 2.5, 220)
    y = np.linspace(-2.5, 2.5, 220)
    X, Y = np.meshgrid(x, y)
    Z = A[0, 0] * X ** 2 + 2 * A[0, 1] * X * Y + A[1, 1] * Y ** 2

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.plot_surface(X, Y, Z)
    ax.set_title(title)

    # ---- Save to folder ----
    save_path = os.path.join("figures", f"{filename}.png")
    plt.savefig(save_path, dpi=300, bbox_inches="tight")
    print(f"✅ Saved: {save_path}")

    plt.show()  # comment out if you only want saving


if __name__ == "__main__":

    matplotlib.use("TkAgg")

    A_PD = np.array([[3, 0.2], [0.2, 2]])
    A_PSD = np.array([[2, -2], [-2, 2]])
    A_ND = np.array([[-3, 0], [0, -1.5]])
    A_IND = np.array([[1, 2], [2, -3]])

    mats = {"PD": A_PD, "PSD": A_PSD, "ND": A_ND, "Indef": A_IND}

    for name, M in mats.items():
        typ, eig = classify(M)
        print(f"{name}: {typ}, eigenvalues = {eig}")

    plotA(A_PD, "PD: convex bowl", "PD_convex_bowl")
    plotA(A_PSD, "PSD: flat ridge", "PSD_flat_ridge")
    plotA(A_ND, "ND: concave bowl", "ND_concave_bowl")
    plotA(A_IND, "Indefinite: saddle", "Indefinite_saddle")
