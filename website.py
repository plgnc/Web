import streamlit as st

# Sidebar navigation
st.sidebar.title("Basketball Website Navigation")
page = st.sidebar.radio("Go to:", ["Home", "Favorites", "Dream/Journey", "About"])

# --- HOME PAGE ---
if page == "Home":
    st.title("🏀 Welcome to Basketball World")
    st.write("Basketball is a fast-paced sport played by two teams of five players. "
             "The objective is to score points by shooting the ball through the opponent's hoop. "
             "It is one of the most popular sports worldwide, known for its excitement, teamwork, and athleticism.")

    st.write("In the Philippines, basketball is more than just a sport, it’s part of the culture. "
             "From barangay courts to professional leagues, Filipinos are passionate about the game. "
             "Local leagues like the PBA, NCAA Philippines, and UAAP showcase homegrown talent, while international competitions like the NBA, FIBA, Japan B.League, and KBL inspire fans everywhere.")

    st.write("Basketball is also a hobby for millions of people. Whether playing pickup games with friends, watching highlights, or following your favorite team, "
             "the sport brings communities together and inspires dreams of becoming a player, coach, or lifelong fan.")

    # Header for totals
    st.subheader("📊 Total Number of Teams in their league (2026)")

    # Quick stats
    col1, col2, col3, col4, col5 = st.columns(5)
    col1.metric("NBA", 30)
    col2.metric("PBA", 13)
    col3.metric("Japan B.League", 24)
    col4.metric("KBL", 10)
    col5.metric("FIBA Nations", 212)

    # Replace slider with a bar chart
    st.subheader("📈 Team Comparison by League")
    team_data = {
        "NBA": 30,
        "PBA": 13,
        "Japan B.League": 24,
        "KBL": 10,
        "FIBA Nations": 212
    }
    st.bar_chart(team_data)

    st.subheader("Some Trivia!")
    with st.expander("🏀 Did you know?"):
        st.write("The first basketball game in 1891 used a soccer ball and two peach baskets!")
        st.write("Dr. James Naismith invented basketball in Springfield, Massachusetts as a way to keep students active indoors during winter.")
        st.write("The original game had 13 rules, and players weren’t allowed to dribble—only pass!")
        st.write("The first professional league, the National Basketball League (NBL), was founded in 1898.")
        st.write("The NBA was formed in 1946 as the Basketball Association of America (BAA) before merging with the NBL in 1949.")


    # Call-to-action button
    if st.button("Go to Favorites"):
        st.write("Navigate to the Favorites page using the sidebar!")

# --- FAVORITES PAGE ---
elif page == "Favorites":
    st.title("❤️ Your Basketball Favorites 💯")

    league = st.radio("Choose your favorite league:", 
                      ["NBA", "PBA", "NCAA (Philippines)", "UAAP (Philippines)", "FIBA", "Japan B.League", "KBL"])

    if league == "NBA":
        team = st.selectbox("Choose your favorite NBA team:", 
                            ["Lakers", "Warriors", "Celtics", "Heat", "Bulls", "Spurs", 
                             "Denver Nuggets", "OKC Thunder", "Brooklyn Nets", "Phoenix Suns"])
        arena = st.selectbox("Choose your favorite arena/stadium:", 
                             ["Madison Square Garden", "Chase Center", "Staples Center", "United Center", "TD Garden"])
        rivalry = st.selectbox("Pick your favorite rivalry:", 
                               ["Lakers vs Celtics", "Warriors vs Cavaliers", "Bulls vs Pistons", 
                                "Heat vs Mavericks", "Knicks vs Nets", "Suns vs Spurs"])

    elif league == "PBA":
        team = st.selectbox("Choose your favorite PBA team:", 
                            ["Barangay Ginebra", "San Miguel Beermen", "TNT Tropang Giga", "Magnolia Hotshots", 
                             "Meralco Bolts", "Rain or Shine", "NorthPort Batang Pier", "Phoenix Fuel Masters", 
                             "Blackwater Bossing", "Terrafirma Dyip"])
        arena = st.selectbox("Choose your favorite arena:", 
                             ["Philippine Arena", "MOA Arena", "Philsports Arena", "Ynares Center Antipolo", "Smart Araneta Coliseum"])
        rivalry = st.selectbox("Pick your favorite rivalry:", 
                               ["Ginebra vs San Miguel", "TNT vs Magnolia", "Alaska vs Purefoods", 
                                "Meralco vs Ginebra", "Rain or Shine vs San Miguel", "Phoenix vs NorthPort"])

    elif league == "NCAA (Philippines)":
        team = st.selectbox("Choose your favorite NCAA team:", 
                            ["San Beda Red Lions", "Letran Knights", "Mapua Cardinals", "Perpetual Altas", 
                             "San Sebastian Stags", "Arellano Chiefs", "JRU Heavy Bombers", "EAC Generals", 
                             "Lyceum Pirates", "CSB Blazers"])
        arena = st.selectbox("Choose your favorite arena:", 
                             ["Philippine Arena", "MOA Arena", "Philsports Arena", "Ynares Center Antipolo", "Smart Araneta Coliseum"])
        rivalry = st.selectbox("Pick your favorite rivalry:", 
                               ["San Beda vs Letran", "Mapua vs San Sebastian", "Lyceum vs CSB", 
                                "Perpetual vs Arellano", "San Sebastian vs JRU", "EAC vs Lyceum"])

    elif league == "UAAP (Philippines)":
        team = st.selectbox("Choose your favorite UAAP team:", 
                            ["Ateneo Blue Eagles", "La Salle Green Archers", "UP Fighting Maroons", "UST Growling Tigers", 
                             "FEU Tamaraws", "Adamson Soaring Falcons", "NU Bulldogs", "UE Red Warriors", 
                             "DLSU Lady Archers", "Ateneo Lady Eagles"])
        arena = st.selectbox("Choose your favorite arena:", 
                             ["Philippine Arena", "MOA Arena", "Philsports Arena", "Ynares Center Antipolo", "Smart Araneta Coliseum"])
        rivalry = st.selectbox("Pick your favorite rivalry:", 
                               ["Ateneo vs La Salle", "UP vs UST", "FEU vs UE", 
                                "NU vs Adamson", "Ateneo vs UP", "La Salle vs FEU"])

    elif league == "FIBA":
        team = st.selectbox("Choose your favorite FIBA team:", 
                            ["USA", "Spain", "Philippines", "Argentina", "France", "Canada", "Greece", "China", "Brazil", "Australia"])
        arena = st.selectbox("Choose your favorite arena/stadium:", 
                             ["Philippine Arena", "Lusail Arena", "Staples Center", "O2 Arena London", "Tokyo Dome"])
        rivalry = st.selectbox("Pick your favorite rivalry:", 
                               ["USA vs Spain", "Philippines vs China", "Argentina vs Brazil", 
                                "France vs Greece", "Canada vs Australia", "USA vs Argentina"])

    elif league == "Japan B.League":
        team = st.selectbox("Choose your favorite B.League team:", 
                            ["Alvark Tokyo", "Ryukyu Golden Kings", "Nagoya Diamond Dolphins", "Osaka Evessa", 
                             "Shibuya Sun Rockers", "Chiba Jets", "Shimane Susanoo Magic", "Niigata Albirex BB", 
                             "Akita Northern Happinets", "Gunma Crane Thunders"])
        arena = st.selectbox("Choose your favorite arena:", 
                             ["Ariake Coliseum", "Okinawa Arena", "Nagoya Civic Arena", "Chiba Port Arena", "Osaka Municipal Gymnasium"])
        rivalry = st.selectbox("Pick your favorite rivalry:", 
                               ["Alvark Tokyo vs Chiba Jets", "Ryukyu vs Nagoya", "Osaka vs Shibuya", 
                                "Akita vs Niigata", "Shimane vs Gunma", "Tokyo vs Ryukyu"])

    elif league == "KBL":
        team = st.selectbox("Choose your favorite KBL team:", 
                            ["Seoul SK Knights", "Busan KT Sonicboom", "Anyang KGC", "Ulsan Hyundai Mobis Phoebus", 
                             "Changwon LG Sakers", "Jeonju KCC Egis", "Wonju DB Promy", "Goyang Orion Orions", 
                             "Daegu KOGAS Pegasus", "Suwon KT Sonicboom"])
        arena = st.selectbox("Choose your favorite arena:", 
                             ["Jamsil Arena", "Busan Sajik Arena", "Anyang Gymnasium", "Changwon Gymnasium", "Ulsan Dongchun Gymnasium"])
        rivalry = st.selectbox("Pick your favorite rivalry:", 
                               ["Seoul SK vs Anyang KGC", "Busan KT vs Ulsan Hyundai", "Changwon vs Jeonju", 
                                "Wonju vs Goyang", "Daegu vs Suwon", "Seoul SK vs Busan KT"])

     # Existing inputs
    player = st.text_input("Enter your favorite basketball player")
    coach = st.text_input("Enter your favorite basketball coach")

    # Single text box for personal reason
    why_favorite = st.text_area("📄 Why are they your favorites?")

    if player and team:
        st.write(f"Awesome! Your favorite player is **{player}**, your favorite team is **{team}**, and your favorite coach is **{coach}**.")
        st.write(f"You follow the **{league}** league, love games at **{arena}**, and enjoy the rivalry **{rivalry}**.")

    if why_favorite:
        st.write(f"📝 Your reason why it is your favorite: {why_favorite}")

# --- DREAM/JOURNEY PAGE ---
elif page == "Dream/Journey":
    st.title("⛹️ Your Basketball Dream & Journey 🏆") 
    st.write("Basketball inspires many dreams, from becoming a professional player to coaching, or simply enjoying the game with friends. "
             "Here, you can share not only your dream but also your journey in basketball.")

    dream_choice = st.selectbox("Choose your basketball dream:", ["Become a pro player", "Coach a team", "Play for fun", "Be a lifelong fan"])
    dream_text = st.text_area("Write something about your dream or own journey to this sport.")

    position = st.radio("Pick your favorite position:", ["Point Guard", "Shooting Guard", "Small Forward", "Power Forward", "Center"])
    jersey_color = st.color_picker("Pick your favorite jersey color")
    start_year = st.number_input("When did you start learning basketball? (Year)", min_value=1950, max_value=2026, step=1)
    place = st.text_input("Where did you first learn to play basketball?")
    influence = st.text_input("Who influenced you to play basketball?")

    if dream_choice or dream_text or start_year or place or influence or position or jersey_color:
        st.write("Here’s your basketball journey/dream:")
        if dream_choice:
            st.write(f"- Dream choice: {dream_choice}")
        if dream_text:
            st.write(f"- Personal dream/journey: {dream_text}")
        if position:
            st.write(f"- Favorite position: {position}")
        if jersey_color:
            st.write(f"- Favorite jersey color: {jersey_color}")
        if start_year:
            st.write(f"- Started learning in: {start_year}")
        if place:
            st.write(f"- Learned at: {place}")
        if influence:
            st.write(f"- Influenced by: {influence}")

        quotes = {
          "Become a pro player": "💬 Quote: \"Every pro was once a beginner.\"",
            "Coach a team": "💬 Quote: \"A good coach can change a game, a great coach can change a life.\"",
            "Play for fun": "💬 Quote: \"Basketball is joy in motion.\"",
            "Be a lifelong fan": "💬 Quote: \"Fans are the heartbeat of the game.\""
}

        if dream_choice in quotes:
           st.markdown(quotes[dream_choice])



# --- ABOUT PAGE ---
elif page == "About":
    st.title("ℹ️ About ")
    st.subheader("What this app does")
    st.write("This app is a simple website that lets you explore basketball basics, share your favorites, and express your basketball dreams and journey.")

    st.subheader("Target Users")
    st.write("Basketball fans, students, and anyone curious about the sport.")

    st.subheader("Inputs Collected")
    st.write("- Favorite league, favorite team, favorite player, coach, arena, rivalry, basketball dream, journey details, favorite position, favorite jersey color.")

    st.subheader("Outputs Shown")
    st.write("- Personalized messages, basketball information, and your dream journey.")

    feedback = st.text_area("💬 Share your feedback or suggest new features/leagues:")
    if st.button("Submit Feedback"):
        st.success("Thank you for your feedback! We’ll use it to improve the app.")
  