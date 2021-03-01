module.exports = class Echo {
    constructor () {

    }

    setString(str) {
        this.text = str;
    }

    getString() {
        if (this.text == null)
        {
            return "<nothing>";
        }
        else
        {
            return this.text;
        }
    }
}



