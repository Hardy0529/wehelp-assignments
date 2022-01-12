// 選單開合
let menu_toggle = document.querySelector("#menu-toggle");
let popup_nav = document.querySelector("#overlay");

let handler = function () {
  popup_nav.classList.toggle("show");
};

menu_toggle.addEventListener("click", handler);

// showMore;
btnMore = document.querySelector("#btnMore");

btnMore.addEventListener("click", showMore);

// 展示更多
let showStart = 0;
let showEnd = 8;
function showMore() {
  showStart += 8;
  showEnd += 8;
  request();
}

// // XMLHttpRequest
function reqListener() {
  let data = this.responseText;
  var plainObj = JSON.parse(data);
  let gallery_item = document.querySelector("#gallery_item");

  obj = plainObj.result.results;
  // 隱藏展示更多按鈕
  if (showEnd > obj.length) {
    showEnd = obj.length;
    btnMore.classList.add("u-hidden");
  }
  for (let i = showStart; i < showEnd; i++) {
    let stitle = obj[i].stitle;

    let img = obj[i].file;
    let imgSeparation = img.split("https");
    let imgSeparationFirst = imgSeparation[1];
    img = "https" + imgSeparationFirst;

    //畫廊HTML
    let col = document.createElement("div");
    col.className = "col";
    // 內層
    let item = document.createElement("div");
    item.className = "gallery-card";
    col.appendChild(item);

    let imgbox = document.createElement("div");
    imgbox.className = "imgbox";
    item.appendChild(imgbox);

    let gallery_card_content = document.createElement("div");
    gallery_card_content.className = "gallery-card_content";
    gallery_card_content.textContent = stitle;
    item.appendChild(gallery_card_content);

    let imgbox_inner = document.createElement("div");
    imgbox_inner.className = "imgbox__inner imgbox__inner-4-3";
    imgbox.appendChild(imgbox_inner);

    let image = document.createElement("div");
    image.className = "image";
    image.style.backgroundImage = `url(${img})`;
    imgbox_inner.appendChild(image);

    gallery_item.appendChild(col);
  }
}
function request() {
  //XMLHttpRequest
  var req = new XMLHttpRequest();
  req.open(
    "get",
    "https://padax.github.io/taipei-day-trip-resources/taipei-attractions-assignment.json"
  );
  req.addEventListener("load", reqListener);
  req.send(); //送出連線
}
request();
