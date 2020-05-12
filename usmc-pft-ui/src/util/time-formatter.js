import React from "react";
import Cleave from "cleave.js/react";

export const RunRowTime = (props) => {
  const { inputRef, ...rest } = props;
  return <Cleave options={{ time: true, timePattern: ["m", "s"] }} {...rest} />;
};
