<script setup lang="ts">
import type { Game } from '../utils/websocket';


const props = defineProps<{game:Game, cellSize:number}>()

const pieces = [
  {
    name: "spider",
    x: 1,
    y: 1
  }
]

const boardPieces = pieces.map((piece) => ({
  name: piece.name,
  style: {
    top: `${piece.y * (props.cellSize*Math.sqrt(3)-1)+(piece.x%2?props.cellSize*Math.sqrt(3)/2:0)}px`,
    left: `${piece.x * (props.cellSize*1.5)}px`
  }
}))
</script>

<template>
  <div class="w-full flex flex-col items-center">
    <div class="text-amber-400 text-6xl">Board</div>
    <button @click="game.click">Click</button>
    <div class="text-2xl">{{ game.messege }}</div>
    <div class=" bg-white border-4 border-gray-600 rounded-md mt-10 h-180 overflow-auto flex relative" :style="{'--size': cellSize + 'px'}">
      <!-- cells -->
      <div v-for="col_idx in 10" :class="$style.col">
        <div v-for="_row_idx in 10" :class="[$style.cell, col_idx % 2 ? ' bg-gray-100' : ' bg-gray-200']"></div>
      </div>

      <!-- pieces -->
      <div>
        <div v-for="piece in boardPieces" :data-name="piece.name" :class="$style.piece" :style="piece.style"></div>
      </div>
    </div>
  </div>
</template>

<style module>
.piece {
  @apply absolute bg-no-repeat bg-center;
  width: calc(var(--size) * 2);
  height: calc(var(--size) * sqrt(3));
  clip-path: polygon(25% 0%, 75% 0%, 100% 50%, 75% 100%, 25% 100%, 0% 50%);
  background-size: calc(var(--size) * 1.95);
  &[data-name="spider"] {
    background-image: url("../assets/spider.jpg");
  }
}

.col:nth-child(even) {
  translate: 0 calc(var(--size) * sqrt(3) / 2);
}
.col:not(:first-child) {
  margin-left: calc(var(--size) / -2);
}

.cell {
  width: calc(var(--size) * 2);
  height: calc(var(--size) * sqrt(3));
  clip-path: polygon(25% 0%, 75% 0%, 100% 50%, 75% 100%, 25% 100%, 0% 50%);
  &:not(:first-child) {
    margin-top: -1px;
  }
}
</style>