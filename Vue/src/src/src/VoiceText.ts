export default class VoiceText {
    private text: string | undefined;
    constructor(text: string) {
        this.text = text;
        alert(`text -> ${text}`)
    }
}