<template>
  <div>
    <h1>Voice Text音声合成</h1>
    <form action="">
      <div>
        <ul>
          <li>
            <label for="">APIキー</label>
            <input type="text" name="apiKey" id="" required />
          </li>
          <li>
            <label for="">テキスト</label>
            <input type="text" name="text" id="" required />
          </li>
          <li>
            <label for="">スピーカー</label>
            <select name="speaker" id="" required>
              <option value="" disabled selected>選択して下さい</option>
              <option value="show">ショウ</option>
              <option value="haruka">ハルカ</option>
              <option value="hikari">ヒカリ</option>
              <option value="takeru">タケル</option>
              <option value="santa">サンタ</option>
              <option value="bear">クマ</option>
            </select>
          </li>
          <li>
            <label for="">感情</label>
            <select name="emotion" id="">
              <option value="" disabled selected>選択して下さい</option>
              <option value="happiness">喜</option>
              <option value="anger">怒</option>
              <option value="sadness">悲</option>
            </select>
          </li>
          <li>
            <label for="">感情レベル</label>
            <input
              type="range"
              name="emotionLevel"
              id=""
              value="2"
              min="1"
              max="4"
              step="1"
            />
            <span></span>
          </li>
          <li>
            <label for="">ピッチ</label>
            <input
              type="range"
              name="pitch"
              value="100"
              min="50"
              max="200"
              step="1"
            />
            <span></span>
          </li>
          <li>
            <label for="">スピード</label>
            <input
              type="range"
              name="speed"
              value="100"
              min="50"
              max="400"
              step="1"
            />
            <span></span>
          </li>
          <li>
            <label for="ボリューム"></label>
            <input
              type="range"
              name="volume"
              value="100"
              min="50"
              max="200"
              step="1"
            />
            <span></span>
          </li>
        </ul>
      </div>
      <button type="submit">送信</button>
    </form>
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
<style scoped></style>
