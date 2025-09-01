# thebirthday

## Overview

Happy Birthday, Somu! 🎉

This project is a heartfelt digital surprise created just for you by me. It's more than just code—it's a celebration of our friendship, the laughs, the deep talks, and all the memories we've made together. I hope this little gift brings a smile to your face and makes your special day even brighter. You are truly one of a kind, and I'm grateful for every moment we've shared. 💖

---

## Some Special Code Snippets

<details>
<summary><b>Login Logic (home.py)</b></summary>

```python
if name.lower() == "moochie" and nickname.lower() == "somu":
	with st.spinner("Unlocking the surprise..."):
		time.sleep(2)
	st.session_state.logged_in = True
	st.session_state.username = name
	st.success("Surprise Unlocked!")
	time.sleep(1)
	st.rerun()
else:
	st.error("Incorrect details. Are you sure you're my somu? 🤔")
```
</details>

<details>
<summary><b>Birthday Card Display (home.py)</b></summary>

```python
image_path = "vanitas.jpg"
base64_image = file_to_base64(image_path)
if base64_image:
	birthday_card_html = f"""
	<div class="card">
		<div class="two-column-layout">
			<div class="image-column">
				<img src="data:image/png;base64,{base64_image}" class="column-image">
			</div>
			<div class="text-column">
				<h2 class="birthday-title">Happiest Birthday my Vanitas ✨</h2>
				<p class="birthday-subtitle">(Now quickly check the surprise page!)</p>
			</div>
		</div>
	</div>
	"""
	st.markdown(birthday_card_html, unsafe_allow_html=True)
else:
	st.warning(f"Could not find '{image_path}'.")
```
</details>

<details>
<summary><b>Poem Page Music Player (poem.py)</b></summary>

```python
audio_path = "Smile for You.mp3"
base64_audio = file_to_base64(audio_path)
if base64_audio:
	component_html = f"""
	<div class=\"custom-audio-container\">
		<button id=\"playBtn\" class=\"custom-play-btn\">▶</button>
		<span class=\"custom-audio-text\">Play The Song</span>
	</div>
	<audio id=\"myAudio\" src=\"data:audio/mp3;base64,{base64_audio}\"></audio>
	<script>
		const audio = document.getElementById('myAudio');
		const playBtn = document.getElementById('playBtn');
		playBtn.addEventListener('click', function() {
			if (audio.paused) {
				audio.play();
				playBtn.innerHTML = '❚❚';
			} else {
				audio.pause();
				playBtn.innerHTML = '▶';
			}
		});
		audio.addEventListener('ended', function() {
			playBtn.innerHTML = '▶';
			audio.currentTime = 0;
		});
	</script>
	"""
	st.components.v1.html(component_html, height=90)
else:
	st.warning(f"Could not find '{audio_path}'.")
```
</details>

---

Made with ❤️ by Rosy, for Somu.