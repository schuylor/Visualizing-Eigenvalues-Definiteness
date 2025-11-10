## Visualizing Eigenvalues & Definiteness

This project visualizes the quadratic form `xᵀ A x` and the surface `z = xᵀ A x` for symmetric matrices `A ∈ R^{2×2}`.

Rather than memorizing linear algebra definitions, we *see* eigenvalues and curvature.

---

## Why visualize eigenvalues?

For any non-zero vector `x`:

`xᵀ A x ≥ 0`  → A is Positive Semi-Definite (PSD)  
all eigenvalues `> 0` → Positive Definite (PD)

Eigenvalues correspond to **curvature**:

| Matrix Type | Eigenvalues | Geometry |
|---|---|---|
Positive Definite (PD) | all > 0 | Convex bowl |
Positive Semi-Definite (PSD) | ≥ 0 and some = 0 | Bowl with flat directions |
Negative Definite (ND) | all < 0 | Upside-down bowl |
Indefinite | mixed signs | Saddle |

Why this matters:

- Convexity in optimization  
- Hessian eigenvalues in machine learning  
- `Xᵀ X` in regression is PSD  
- Ridge regression lifts eigenvalues (`A + λI`)  

We treat linear algebra not as symbols, but as **geometry and curvature**.
