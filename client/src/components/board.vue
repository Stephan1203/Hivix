<script setup lang="ts">
import type { Game } from '../utils/websocket';


defineProps<{game:Game}>()
</script>

<template>
  <div class="w-full flex flex-col items-center">
    <div class="text-amber-400 text-6xl">Board</div>
    <button @click="game.click">Click</button>
    <div class="text-2xl">{{ game.messege }}</div>
  </div>
</template>