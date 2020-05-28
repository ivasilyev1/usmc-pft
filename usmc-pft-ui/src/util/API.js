const requestHeaders = {
  "Access-Control-Allow-Origin": "*",
  "Content-Type": "application/json",
};

const request = async (endpoint, method, body) => {
  //const url = `https://usmcpft.com/api/${endpoint}`;
  const url = `http://127.0.0.1:5000/api/${endpoint}`;
  let response = await fetch(url, {
    headers: requestHeaders,
    method: method,
    body: body,
  });
  return response.json();
};

export const getPFTScores = async (scores) => {
  let eventScores = {};
  eventScores[scores.firstEvent] = scores.firstEventCount;
  eventScores[scores.secondEvent] = scores.secondEventCount;
  eventScores[scores.thirdEvent] = scores.thirdEventCount;
  eventScores["age"] = scores.age;
  eventScores["high_alt"] = scores.high_alt;
  eventScores["gender"] = scores.gender;
  const body = JSON.stringify(eventScores);
  let response = await request("pft", "POST", body);
  return response;
};

export const getCFTScores = async (scores) => {
  const body = JSON.stringify({
    mtc: scores.mtc,
    muf: scores.muf,
    ammo: scores.ammo,
    age: scores.age,
    high_alt: scores.high_alt,
    gender: scores.gender,
  });
  let response = await request("cft", "POST", body);
  return response;
};
