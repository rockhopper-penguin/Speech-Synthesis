<template>
  <div>
    <h1>Voice Text音声合成</h1>
  </div>
</template>

<script lang="ts">
import { Component, Prop, Vue } from "vue-property-decorator";
import VoiceText from "../src/VoiceText";

@Component
export default class Main extends Vue {
  constructor() {
    super();
    const text = "ボイステキストクラス";
    const voiceText = new VoiceText(text);
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
</style>
