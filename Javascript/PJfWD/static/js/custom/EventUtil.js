/**
* 跨浏览器方法
*
*/

var EventUtil = {
    addHandler: function(element, type, handler) {
        if (element.addEventListener) {
            // 如果存在DOM2级方法,则使用该方法,参数:
            //传输事件类型, 事件处理函数和第三个参数false(表示在冒泡阶段触发)
            element.addEventListener(type, handler, false);
        } else if (element.attachEvent) {
            // IE中要加上on方法
            element.attachEvent("on" + type, handler);
        } else {
            // 默认方法
            element["on" + type] = handler;
        }
    },

    getEvent: function(event) {
        return event? event : window.event;
    },

    getTarget: function(event) {
        return event.target || event.srcElement;
    },

    getCharCode: function(event){
        //以跨浏览器取得相同的字符编码，需在keypress事件中使用
        if(typeof event.charCode=="number"){
                 return event.charCode;
             }else{
                return event.keyCode;
             }
    },

    getClipboardText: function(event) {
        var clipboardDate = (event.clipboardDate || window.clipboardDate);
        return clipboardDate.getDate("text");
    },

    setClipboardText: function(event) {
        if (event.clipboardDate) {
            //Chrome, Safari
            return event.clipboardDate.setData("text/plain", value);
        } else if (window.clipboardDate) {
            //IE
            return window.clipboardDate.setData("text", value);
        }
    },

    preventDefault: function(event) {
            if (event.preventDefault) {
                event.preventDefault();
            } else {
                event.returnValue = false;
            }
        },

    removeHandler: function(element, type, handler) {
                    if (element.removeEventListener) {
                        element.removeEventListener(type, handler, false);
                    } else if (element.detachEvent) {
                        element.detachEvent("on" + type, handler);
                    } else {
                        element["on" + type] = null;
                    }
                },

    stopPropagation: function(event) {
        if (event.stopPropagation) {
            event.stopPropagation();
        } else {
            event.cancelBubble = true;
        }
    }
}
