// 連線一

function queryUserNameFun(queryUserName) {
  return new Promise(function (resolve, reject) {
    var req = new XMLHttpRequest();
    req.open(
      "get",
      "http://127.0.0.1:3000/api/members?username=" + queryUserName
    );
    req.addEventListener("load", function () {
      resolve(this.responseText);
    });

    req.send();
  });
}

const queryUserNameButton = document.querySelector("#queryUserNameButton");
queryUserNameButton.addEventListener("click", queryUserName);

function queryUserName() {
  const queryUserName = document.querySelector("#queryUserName").value;

  queryUserNameFun(queryUserName).then(function (result) {
    const queryUserNameShow = document.querySelector("#queryUserNameShow");
    const resultData = JSON.parse(result);
    if (resultData.data == null) {
      queryUserNameShow.innerHTML = "無此資料";
    } else {
      const resultDataName = resultData.data.name;
      queryUserNameShow.innerHTML = resultDataName;
    }
  });
}
