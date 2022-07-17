FINDER_CLASS = """
class Finder {
    constructor(targetText) {
        this.targetText = targetText;
        this.gtButtons = [];
        this.buttons = [];
        this.targetButtonIndex = -1;
    }

    find() {
        this.gtButtons = [];
        this.buttons = [];
        this.targetButtonIndex = -1;
        this.loadGtButtons();
        this.findButtons();
    }

    loadGtButtons() {
        const allButtons = document.getElementsByTagName("gt-button");
        for(var i=0; i<allButtons.length; i++) {
            this.gtButtons.push(allButtons.item(i));
        }
    }

    findButtons() {
        this.gtButtons.forEach(item => {
            const children = item.shadowRoot.children;
            for(var i=0; i<children.length; i++) {
                if (children.item(i).type == "button") {
                    this.buttons.push(children.item(i));
                }
            }
        })
    }

    hasTarget() {
        var result = false;

        for(var i=0; i < this.buttons.length; i++) {
            if (this.buttons[i].innerText.toLowerCase() == this.targetText.toLowerCase()) {
                result = true;
                this.targetButtonIndex = i;
                break;
            }
        }

        return result;
    }

    click() {
        this.buttons[this.targetButtonIndex].click();
    }
}
"""

SIGN_IN_EXISTS = """

var finder = new Finder("sign in");
finder.find();
return finder.hasTarget();
"""

SIGN_IN_CLICK = """

var finder = new Finder("sign in");
finder.find();
if (finder.hasTarget()){
    finder.click();
}
"""

SIGN_OUT_EXISTS = """

var finder = new Finder("sign out");
finder.find();
return finder.hasTarget();
"""

SIGN_OUT_CLICK = """

var finder = new Finder("sign out");
finder.find();
if (finder.hasTarget()){
    finder.click();
}
"""