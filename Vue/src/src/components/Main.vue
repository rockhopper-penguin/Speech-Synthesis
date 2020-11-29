<template>
  <div id="main">
    <h1>Voice Text音声合成</h1>
    <form action="">
      <div>
        <ul>
          <li>
            <label for="">APIキー</label>
            <input type="text" name="apiKey" id="" v-model="apiKey" required />
          </li>
          <li>
            <label for="">テキスト</label>
            <input type="text" name="text" id="" v-model="text" required />
          </li>
          <li>
            <label for="">スピーカー</label>
            <select
              name="speaker"
              id=""
              v-model="speaker"
              @change="changeSpeaker"
              required
            >
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
            <select
              name="emotion"
              id=""
              v-model="emotion"
              v-bind:disabled="isShow"
            >
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
              v-model="emotionLevel"
            />
            <span>{{ emotionLevel }}</span>
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
              v-model="pitch"
            />
            <span>{{ pitch }}</span>
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
              v-model="speed"
            />
            <span>{{ speed }}</span>
          </li>
          <li>
            <label for="">ボリューム</label>
            <input
              type="range"
              name="volume"
              value="100"
              min="50"
              max="200"
              step="1"
              v-model="volume"
            />
            <span>{{ volume }}</span>
          </li>
        </ul>
      </div>
      <div id="send-button">
        <button type="submit" v-on:click="test">送信</button>
      </div>
    </form>
  </div>
</template>

<script lang="ts">
import { Component, Prop, Vue } from "vue-property-decorator";
import VoiceText from "../src/VoiceText";

@Component
export default class Main extends Vue {
  /** APIキー */
  private apiKey = "";
  /** テキスト */
  private text = "";
  /** スピーカー */
  private speaker = "";
  /** 感情 */
  private emotion = "";
  /** 感情レベル */
  private emotionLevel = 2;
  /** ピッチ */
  private pitch = 100;
  /** スピード */
  private speed = 100;
  /** ボリューム */
  private volume = 100;
  /** 選択されたスピーカーがショウかどうか(ショウだと感情設定ができない) */
  private isShow = false;

  private voiceText: any;
  constructor() {
    super();
  }

  async test() {
    // alert(`apiKey : ${this.apiKey}`);
    const voiceText = await new VoiceText(this.text);
    const test = await voiceText.test();
    if (test) {
      alert("Test method execution is successfull");
    }
  }

  changeSpeaker() {
    if (this.speaker == "show") {
      this.isShow = true;
      return;
    }
    this.isShow = false;
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
#main {
  width: 80%;
  margin: auto;
}

#main h1,
#send-button {
  text-align: center;
}

#send-button button {
  border: none;
  padding: 10px;
  border-radius: 5px;
}

ul li,
label,
span {
  margin: 10px;
}
</style>
