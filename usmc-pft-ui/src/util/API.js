const requestHeaders = {
  "Access-Control-Allow-Origin": "*",
  "Content-Type": "application/json",
};

const request = async (endpoint, method, body) => {
  const url = `http://127.0.0.1:5000/api/${endpoint}`;
  let response = await fetch(url, {
    headers: requestHeaders,
    method: method,
    body: body,
  });
  return response.json();
};

export const getTestScores = async (test, scores) => {
  const endpoint = test;
  let eventScores = {};
  //console.log(scores);
  eventScores[scores.cardio] = scores.cardioTime;
  eventScores[scores.upperBody] = scores.upperBodyReps;
  eventScores[scores.abdominal] = scores.abReps;
  eventScores["age"] = scores.age;
  eventScores["high_alt"] = scores.high_alt;
  eventScores["gender"] = scores.gender;
  //console.log(eventScores);
  const body = JSON.stringify(eventScores);
  let response = await request(endpoint, "POST", body);
  //console.log(response);
  return response;
  //console.log(response);
};
