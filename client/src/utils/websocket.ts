import { ref } from "vue"

export const getGame = () => {
  const ws = new WebSocket("ws://localhost:8765")
  const messege = ref("")
  const pices = ref("")
  const state = ref("")

  ws.onmessage = (event) => {
    const data = JSON.parse(event.data)
    switch(data.type) {
      case "messege": {
        messege.value = data
        break
      }
      case "pices": {
        pices.value = data
        break
      }
      case "state": {
        state.value = data
        break
      }
      default: console.log("Прислали несуществующий тип")
    }
  }

  const click = () => {
    ws.send("Игра началась")
  }

  return {messege, click}
}

export type Game = ReturnType<typeof getGame>