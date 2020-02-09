const Url = "http://localhost:2020/display"
let loaded = 0
let score = 0

function getResults() {
	let request = new XMLHttpRequest()
	request.addEventListener("load", () => {
		console.log(request.status)
		if (request.status != 200) {
			return
		}
		let input = request.response

		let output = input.split(" ")[0]
		score = output
		console.log(score)
		let botboxwords = input.substr(input.indexOf(" ") + 1)

		let name = document.createElement('p')
		let percent = document.createTextNode(output.concat("%"))
		name.appendChild(percent)
		document.getElementById('cornpatibility').appendChild(name)

		let message = document.createElement('p').appendChild(document.createTextNode("It's a patch!"))
		var heartimgl = document.createElement('img')
		var heartimgr = document.createElement('img')
		heartimgl.src = "imgs/heart.png"
		heartimgr.src = "imgs/heart.png"
		if(output < 50) {
			message = document.createElement('p').appendChild(document.createTextNode(botboxwords))
			heartimgl.src = "imgs/broken_heart.png"
			heartimgr.src = "imgs/broken_heart.png"
		}
		document.getElementById('botbox').appendChild(message)
		document.getElementById('heartboxl').appendChild(heartimgl)
		document.getElementById('heartboxr').appendChild(heartimgr)
	})
	request.open('GET', Url)
	request.send()

}

const Url2 = "http://localhost:2020/submit"

function submit() {
	let request = new XMLHttpRequest()
	let name1 = document.getElementById('name1').value
	let name2 = document.getElementById('name2').value
	request.open('POST', Url2)
	request.setRequestHeader("Content-Type", "application/json")
	request.send(`{"name1": "${name1}", "name2": "${name2}", "score": "${score}"}`)
	var element = document.getElementById('submit')
	document.getElementById('submitbutton').removeChild(element)
	var newbutton = document.createElement('input')
	newbutton.id = "submit"
	newbutton.type = "button"
	newbutton.value = "Uploading..."
	document.getElementById('submitbutton').appendChild(newbutton)
	setTimeout(() => { window.location.href = "scoreboard.html"; }, 1000);
}


getResults()