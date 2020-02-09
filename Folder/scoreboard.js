const Url = "http://localhost:2020/get"
let loaded = 0

function getNames() {
	let request = new XMLHttpRequest()
	request.addEventListener("load", () => {
		console.log(request.status)
		if (request.status != 200) {
			return
		}

		let names  = JSON.parse(request.response)

		while (loaded < names.length) {

			let scoreitem = document.createElement('div')
			scoreitem.id = "scoreitem"

			let nameitem = document.createElement('div')
			nameitem.id = "name"
			let name = document.createElement('p')
			let text = document.createTextNode(names[loaded])
			name.appendChild(text)
			nameitem.appendChild(name)
			loaded++;
			scoreitem.appendChild(nameitem)

			nameitem = document.createElement('div')
			nameitem.id = "score"
			name = document.createElement('p')
			text = document.createTextNode(names[loaded].concat("%"))
			name.appendChild(text)
			nameitem.appendChild(name)
			loaded++;
			scoreitem.appendChild(nameitem)

			nameitem = document.createElement('div')
			nameitem.id = "name2"
			scoreitem.appendChild(nameitem)
			name = document.createElement('p')
			text = document.createTextNode(names[loaded])
			name.appendChild(text)
			nameitem.appendChild(name)
			loaded++;

			document.getElementById('scorelist').appendChild(scoreitem)

		}
	})
	request.open('GET', Url)
	request.send()

}

getNames()
setInterval(getNames, 1000)
