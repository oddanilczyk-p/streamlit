

# st.write("Hello word")
# # st.warning("Hello word")
# # st.error("Hello word")
# # st.title("Hello word")
# #
# import streamlit as st
#
# wejscie = st.text_input("Test inputu")
# button = st.button("Test")
# if button:
#     st.title(wejscie)


import streamlit as st

pytania = ["Co jest stolica Polski?", "Ile kontynentow jest na Ziemie", "Ktory pierweiastek chemiczny ma symbol'0'?", "Jaki numer koszulki ma Robert Lewandowski?", " Ile dni ma marzec?", "Kiedy byl chrzest Polski?","Stolica niemiec to: "]
odpowiedzi = [["Warszawa", "Poznan", "Lublin"],["5", "6", "7"], ["Tlen", "Wodor", "Hel"], ["1","4","9"], ["30","31","29"], ["966", "967", "999"], ["Genewa", "Litwa", "Berlin"]]
poprawne = [0,2,0,2,0,0,1]

if "punkty" not in st.session_state:
    st.session_state.punkty = 0
if "pytanie" not in st.session_state:
    st.session_state.pytanie = 0
if "feedback" not in st.session_state:
    st.session_state.feedback = ""

p = st.session_state.pytanie

st.title("🧠 Quiz z wiedzy ogólnej")

if p < len(pytania):
    st.subheader(f"Pytanie {p + 1} z {len(pytania)}")
    st.write(pytania[p])

    wybor = st.radio("Wybierz odpowiedź:", odpowiedzi[p])
#
    if st.button("Zatwierdź odpowiedź"):
        poprawna_odp = odpowiedzi[p][poprawne[p]]
        if wybor == poprawna_odp:
            st.session_state.punkty += 1
            st.session_state.feedback = "✅ Poprawna odpowiedź!"
        else:
            st.session_state.feedback = f"❌ Błędna odpowiedź! Poprawna to: {poprawna_odp}"

        st.session_state.pytanie += 1
        st.rerun()

    if st.session_state.feedback:
        st.info(st.session_state.feedback)

if p == 7:
    punkty = p
    st.title(f"Liczba punktów to: {st.session_state.punkty}")
    if punkty == 7:
        st.write("Dostales ocene A")
    elif punkty == 6:
        st.write("Dostales ocene B")
    elif punkty == 5:
        st.write("Dostales ocene C")
    elif punkty == 4:
        st.write("Dostales ocene D")
    else:
        st.write("Dostales ocene F")



