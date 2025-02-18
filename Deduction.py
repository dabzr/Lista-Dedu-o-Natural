import marimo

__generated_with = "0.11.6"
app = marimo.App(width="medium")


@app.cell
def _():
    from nadia.nadia_pt_fo import check_proof
    return (check_proof,)


@app.cell
def _():
    import marimo as mo
    return (mo,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""## Lista de Dedução Natural""")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        Questão 1

        ∀xP(x) ∨ Q(y) ⊢ ∀x(P(x) ∨ Q(y))
        """
    )
    return


@app.cell(hide_code=True)
def _(check_proof):
    q1 = """
    1. AxP(x) | Q(y)     pre
    2. { a
    3.    { AxP(x)       hip
    4.      P(a)         Ae 3
    5.      P(a) | Q(y)  |i 4
            }
    6.    { Q(y)         hip
    7.      P(a) | Q(y)  |i 6
          }
    8. P(a) | Q(y)       |e 1, 3-5, 6-7
    }
    9. Ax(P(x) | Q(y)) Ai 2-8
    """
    print(q1)
    print(check_proof(q1, display_fitch=False, display_gentzen=False))
    return (q1,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        Questão 2

        ∀x(P(x) ∨ Q(y)) ⊢ ∀xP(x) ∨ Q(y)
        """
    )
    return


@app.cell(hide_code=True)
def _(check_proof):
    q2 = """
    1. Ax(P(x) | Q(y))     pre
    2. { ~(AxP(x) | Q(y))  hip
    3.   { Q(y)            hip
    4.     AxP(x) | Q(y)   |i 3
    5.     @               ~e 2, 4
         }
    6.   ~Q(y)             ~i 3-5
    7.   { a
    8.     P(a) | Q(y)     Ae 1
    9.     {P(a)           hip}
    10.    { Q(y)          hip
    11.     @              ~e 6, 10
    12.     P(a)           @e 11
           }
    13.    P(a)            |e 8, 9-9, 10-12
         }
    14.  AxP(x)            Ai 7-13
    15.  AxP(x) | Q(y)     |i 14
    16.  @                 ~e 2, 15
       }
    17. AxP(x) | Q(y)      raa 2-16
    """
    print(q2)
    print(check_proof(q2, display_fitch=False, display_gentzen=False))
    return (q2,)


if __name__ == "__main__":
    app.run()
