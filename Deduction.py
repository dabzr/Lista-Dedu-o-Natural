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
def _(mo):
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
    mo.show_code()
    return (q1,)


@app.cell(hide_code=True)
def _(check_proof, mo, q1):
    mo.md(check_proof(q1, display_fitch=False, display_gentzen=False))
    return


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
def _(mo):
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
    mo.show_code()
    return (q2,)


@app.cell(hide_code=True)
def _(check_proof, mo, q2):
    mo.md(check_proof(q2, display_fitch=False, display_gentzen=False))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        Questão 3

        ∃xP(x) ∨ ∃xQ(x) ⊢ ∃x(P(x) ∨ Q(x))
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    q3 = """
    1. ExP(x) | ExQ(x)     pre
    2. { ExP(x)            hip
    3.   { a P(a)          hip
    4.     P(a) | Q(a)     |i 3
    5.     Ex(P(x) | Q(x)) Ei 4
         }
    6.   Ex(P(x) | Q(x))   Ee 2, 3-5
       }
    7. { ExQ(x)            hip
    8.   {a Q(a)           hip
    9.    P(a) | Q(a)      |i 8
    10.   Ex(P(x) | Q(x))  Ei 9
         }
    11.  Ex(P(x) | Q(x))   Ee 7, 8-10
       }
    12. Ex(P(x) | Q(x))    |e 1, 2-6, 7-11
    """
    mo.show_code()
    return (q3,)


@app.cell(hide_code=True)
def _(check_proof, mo, q3):
    mo.md(check_proof(q3, display_fitch=False, display_gentzen=False))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        Questão 4

        ∃x(P(x) ∨ Q(x)) ⊢ ∃xP(x) ∨ ∃xQ(x)
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    q4 = """
    1. Ex(P(x) | Q(x))      pre
    2. { a P(a) | Q(a)      hip
    3.   {P(a)              hip
    4.    ExP(x)            Ei 3
    5.    ExP(x) | ExQ(x)   |i 4
         }
    6.   {Q(a)              hip
    7.    ExQ(x)            Ei 6
    8.    ExP(x) | ExQ(x)   |i 7
         }
    9.   ExP(x) | ExQ(x)    |e 2, 3-5, 6-8
      }
    10. ExP(x) | ExQ(x)     Ee 1, 2-9
    """
    mo.show_code()
    return (q4,)


@app.cell(hide_code=True)
def _(check_proof, mo, q4):
    mo.md(check_proof(q4, display_fitch=False, display_gentzen=False))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        Questão 5

        ∃x(P(x) ∧ Q(z)) ⊢ ∃xP(x) ∧ Q(z)
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    q5 = """
    1. Ex(P(x) & Q(z))     pre
    2. { a P(a) & Q(z)     hip
    3.   P(a)              &e 2
    4.   ExP(x)            Ei 3
    5.   Q(z)              &e 2
    6.   ExP(x) & Q(z)     &i 4, 5
       }
    7. ExP(x) & Q(z)       Ee 1, 2-6
    """
    mo.show_code()
    return (q5,)


@app.cell(hide_code=True)
def _(check_proof, mo, q5):
    mo.md(check_proof(q5, display_fitch=False, display_gentzen=False))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        Questão 6

        ∃xP(x) ∧ Q(z) ⊢ ∃x(P(x) ∧ Q(z))
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    q6 = """
    1. ExP(x) & Q(z)     pre
    2. ExP(x)            &e 1
    3. { a P(a)          hip
    4.   Q(z)            &e 1
    5.   P(a) & Q(z)     &i 3, 4
    6.   Ex(P(x) & Q(z)) Ei 5
       }
    7. Ex(P(x) & Q(z))   Ee 2, 3-6
    """
    mo.show_code()
    return (q6,)


@app.cell(hide_code=True)
def _(check_proof, mo, q6):
    mo.md(check_proof(q6, display_fitch=False, display_gentzen=False))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        Questão 7

        Q(y) → ∀xP(x) ⊢ ∀x(Q(y) → P(x))
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    q7 = """
    1. Q(y) -> AxP(x)    pre
    2. { a
    3.   { Q(y)          hip
    4.     AxP(x)        ->e 1, 3
    5.     P(a)          Ae 4
         }
    6.   Q(y) -> P(a)    ->i 3-5
        }
    7.  Ax(Q(y) -> P(x)) Ai 2-6
    """
    mo.show_code()
    return (q7,)


@app.cell(hide_code=True)
def _(check_proof, mo, q7):
    mo.md(check_proof(q7, display_fitch=False, display_gentzen=False))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        Questão 8

        ∀x(Q(y) → P(x)) ⊢ Q(y) → ∀xP(x)
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    q8 = """
    1. Ax(Q(y) -> P(x))    pre
    2. {  Q(y)             hip
    3.    { a
    4.      Q(y) -> P(a)   Ae 1
    5.      P(a)           ->e 2,4
          }
    6.    AxP(x)           Ai 3-5
       }
    7. Q(y) -> AxP(x)      ->i 2-6
    """
    mo.show_code()
    return (q8,)


@app.cell(hide_code=True)
def _(check_proof, mo, q8):
    mo.md(check_proof(q8, display_fitch=False, display_gentzen=False))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        Questão 9

        ∀xP(x) → Q(y) ⊢ ∃x(P(x) → Q(y))
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    q9 = """ 
    1. AxP(x) -> Q(y)                    pre
    2. { ~(Ex(P(x) -> Q(y)))             hip
    }
    """
    mo.show_code()
    return (q9,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        Questão 10

        ∃x(P(x) → Q(y)) ⊢ ∀xP(x) → Q(y)
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    q10 = """
    1. Ex(P(x) -> Q(y))         pre
    2. { a P(a)->Q(y)           hip
    3.   {  Ax P(x)             hip
    4.      P(a)                Ae 3
    5.      Q(y)                ->e 2,4
         }
    6.   AxP(x) -> Q(y)         ->i 3-5
       }
    7. AxP(x) -> Q(y)           Ee  1, 2-6
    """
    mo.show_code()
    return (q10,)


@app.cell(hide_code=True)
def _(check_proof, mo, q10):
    mo.md(check_proof(q10, display_fitch=False, display_gentzen=False))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        Questão 11

        ∀x(P(x) → Q(y)) ⊢ ∃xP(x) → Q(y)
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    q11 = """
    1. Ax(P(x) -> Q(y))   pre
    2. { ExP(x)           hip
    3.   { a P(a)         hip
    4.     P(a) -> Q(y)   Ae 1
    5.     Q(y)           ->e 3,4
         }
    6.   Q(y)             Ee 2, 3-5
       }
    7. ExP(x) -> Q(y)     ->i 2-6
    """
    mo.show_code()
    return (q11,)


@app.cell(hide_code=True)
def _(check_proof, mo, q11):
    mo.md(check_proof(q11, display_fitch=False, display_gentzen=False))
    return


if __name__ == "__main__":
    app.run()
