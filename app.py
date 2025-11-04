import streamlit as st

# Titolo e descrizione
st.title("Calcolo eccentricità fondazione superficiale")
st.write("App per il calcolo di Ex ed Ey a partire da V, Mx, My e le dimensioni B, H.")

# Input dei dati
B = st.number_input("Larghezza B [m]", min_value=0.0, value=2.0, step=0.1)
H = st.number_input("Lunghezza H [m]", min_value=0.0, value=3.0, step=0.1)
V = st.number_input("Sforzo normale V [kN]", min_value=0.0, value=1000.0, step=10.0)
Mx = st.number_input("Momento Mx [kNm]", value=50.0, step=1.0)
My = st.number_input("Momento My [kNm]", value=75.0, step=1.0)

# Calcolo eccentricità (con controllo V>0)
if V > 0:
    Ex = My / V
    Ey = Mx / V
    st.subheader("Risultati")
    st.write(f"**Ex = {Ex:.4f} m**")
    st.write(f"**Ey = {Ey:.4f} m**")

    # Controllo se l’eccentricità è entro il nucleo centrale
    st.write("### Verifica nucleo centrale")
    if abs(Ex) <= B / 6 and abs(Ey) <= H / 6:
        st.success("La risultante è interna al nucleo centrale della fondazione ✅")
    else:
        st.warning("La risultante è esterna al nucleo centrale ⚠️")
else:
    st.error("Inserire un valore di V maggiore di zero.")
