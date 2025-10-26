import streamlit as st

st.set_page_config(
    page_title="포켓몬 도감",
    # page_icon="./images/monsterball.png"
    page_icon=".\img\photo-1542779283-429940ce8336.avif"
)

st.title("streamlit 포켓몬 도감")
st.markdown("**포켓몬**을 하나씩 추가해서 도감을 채워보세요!")

type_emoji_dict = {
    "노말": "⚪",
    "격투": "✊",
    "비행": "🕊",
    "독": "☠️",
    "땅": "🌋",
    "바위": "🪨",
    "벌레": "🐛",
    "고스트": "👻",
    "강철": "🤖",
    "불꽃": "🔥",
    "물": "💧",
    "풀": "🍃",
    "전기": "⚡",
    "에스퍼": "🔮",
    "얼음": "❄️",
    "드래곤": "🐲",
    "악": "😈",
    "페어리": "🧚"
}

initial_pokemons = [
    {
        "name": "피카츄",
        "types": ["전기"],
        "image_url": "https://th.bing.com/th/id/OIP.p35r2gGRDUF1v_avXXmmiAHaHa?w=198&h=198&c=7&r=0&o=7&dpr=1.3&pid=1.7&rm=300",
    },
    {
        "name": "누오",
        "types": ["물", "땅"],
        "image_url": "https://th.bing.com/th/id/OIP.i8RZhoRNQTzM_9QNuWPg6AHaFj?w=226&h=180&c=7&r=0&o=7&dpr=1.3&pid=1.7&rm=300",
    },
    {
        "name": "갸라도스",
        "types": ["물", "비행"],
        "image_url": "https://th.bing.com/th/id/OIP.EudmZ2q44IqQS-OnK552FQAAAA?w=164&h=180&c=7&r=0&o=7&dpr=1.3&pid=1.7&rm=300",
    },
    {
        "name": "개굴닌자",
        "types": ["물", "악"],
        "image_url": "https://th.bing.com/th/id/OIP.Yfdl3xWBq_FJ8MrZIOLnXQHaHa?w=155&h=180&c=7&r=0&o=7&dpr=1.3&pid=1.7&rm=300",
    },
    {
        "name": "루카리오",
        "types": ["격투", "강철"],
        "image_url": "https://th.bing.com/th/id/OIP.BP-m8Y_R8tPAdRbvOUcylQHaHa?w=176&h=180&c=7&r=0&o=7&dpr=1.3&pid=1.7&rm=300",
    },
    {
        "name": "에이스번",
        "types": ["불꽃"],
        "image_url": "https://tse2.mm.bing.net/th/id/OIP.JkfVyC0ja8C4qPCKm3bqlQHaEK?rs=1&pid=ImgDetMain&o=7&rm=300",
    },
]

if "pokemons" not in st.session_state:
    st.session_state.pokemons = initial_pokemons

with st.form(key="form"):
    col1, col2 = st.columns(2)
    with col1:
        name = st.text_input(label="포켓몬 이름")
    with col2:
        types = st.multiselect(
            label="포켓몬 속성",
            options=list(type_emoji_dict.keys()),
            max_selections=2,
        )
    image_url = st.text_input(label="포켓몬 이미지 URL")
    submit = st.form_submit_button(label="Submit")
    if submit:
        if not name:
            st.error("포켓몬의 이름을 입력해주세요.")
        elif len(types) == 0:
            st.error("포켓몬의 속성을 적어도 한개 선택해주세요.")
        else:
            st.success("포켓몬을 추가할 수 있습니다.")
            st.session_state.pokemons.append({
                "name": name,
                "types": types,
                "image_url": image_url if image_url else ".\img\photo-1542779283-429940ce8336.avif"
            })

for i in range(0, len(st.session_state.pokemons), 3):
    row_pokemons = st.session_state.pokemons[i:i+3]
    cols = st.columns(3)
    for j in range(len(row_pokemons)):
        with cols[j]:
            pokemon = row_pokemons[j]
            with st.expander(label=f"**{i+j+1}. {pokemon['name']}**", expanded=True):
                st.image(pokemon["image_url"])
                emoji_types = [f"{type_emoji_dict[x]} {x}" for x in pokemon["types"]]
                st.text(" / ".join(emoji_types))