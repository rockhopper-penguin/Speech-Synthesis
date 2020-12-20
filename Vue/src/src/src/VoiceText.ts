import axios from 'axios';

export default class VoiceText {
    private text: string | undefined;
    constructor(text: string) {
        this.text = text;
    }

    test() {
        alert(`text -> ${this.text}`);
        return true
    }
}