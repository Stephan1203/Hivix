<script setup lang="ts">
import { onMounted, ref } from 'vue';
import Board from './components/board.vue';
import Navbar from './components/navbar.vue';
import { getGame } from './utils/websocket.ts';

const game = ref()
onMounted(() => {
  game.value = getGame()
})
</script>

<template>
  <div class="flex h-full">
    <Navbar/>
    <Board v-if="game" :game/>
  </div>
</template>
