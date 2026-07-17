<script setup lang="ts">
</script>

<template>
  <div class="w-80 min-w-80 bg-gray-500 h-full shadow-[0_0_20px] shadow-[#0004]">
    <h1 class="text-6xl font-bold text-gray-300 m-4">Hivix</h1>
    <div class="bg-yellow-400 size-50 m-10" :class="$style.cell"></div>
  </div>
</template>

<style module>
.cell {
  --size: 100px;
  width: calc(var(--size) * 1.732); 
  height: calc(var(--size) * 2);
  clip-path: polygon(50% 0%, 100% 25%, 100% 75%, 50% 100%, 0% 75%, 0% 25%);
}
</style>