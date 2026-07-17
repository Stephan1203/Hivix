import { ref } from "vue"

export const getGame = () => {
  const ws = new WebSocket("ws://localhost:8765")
  const messege = ref("")

  ws.onmessage = (event) => {
    messege.value = event.data
  }

  const click = () => {
    ws.send("Игра началась")
  }

  return {messege, click}
}

export type Game = ReturnType<typeof getGame>