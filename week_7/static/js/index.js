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
queryUserNameButton.addEventListener("click", queryFun);

function queryFun() {
  let queryUserNameValue = document.querySelector("#queryUserName");
  const queryUserName = document.querySelector("#queryUserName").value;

  queryUserNameFun(queryUserName).then(function (result) {
    const queryUserNameShow = document.querySelector("#queryUserNameShow");
    const resultData = JSON.parse(result);
    if (resultData.data == null) {
      queryUserNameShow.innerHTML = "無此資料";
      queryUserNameValue.value = "";
    } else {
      const resultDataName = resultData.data.name;
      queryUserNameShow.innerHTML = resultDataName;
      queryUserNameValue.value = "";
    }
  });
}

// 連線二
function updateUserNameFun(url, data) {
  return fetch(url, {
    body: JSON.stringify(data),
    headers: {
      "content-type": "application/json",
    },
    method: "POST",
  }).then((response) => response.json());
}

const updateUserNameButton = document.querySelector("#updateUserNameButton");
updateUserNameButton.addEventListener("click", updateFun);
function updateFun() {
  let updateUserNameValue = document.querySelector("#updateUserName");
  const updateUserName = document.querySelector("#updateUserName").value;

  const data = {
    updateUserName,
  };

  updateUserNameFun("http://127.0.0.1:3000/api/member", data).then((data) => {
    dataType = data;
    if (dataType.ok == true) {
      const updateUserNameShow = document.querySelector("#updateUserNameShow");
      updateUserNameShow.innerHTML = "更新成功";
      updateUserNameValue.value = "";
    }
  });
}
