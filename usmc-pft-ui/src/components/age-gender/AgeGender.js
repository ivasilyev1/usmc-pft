import React from "react";
import { Select, TextField, Typography } from "@material-ui/core";

import styles from "./AgeGender.module.scss";

const AgeGender = (props) => {
  return (
    <div className={styles.container}>
      <Typography>Age:</Typography>
      <TextField
        id="age"
        name="age"
        type="text"
        inputProps={{
          min: 17,
          max: 99,
          maxLength: 2,
        }}
      />
      <Typography>Gender:</Typography>
      <Select name="gender" defaultValue={"M"} native>
        <option value={"M"}>M</option>
        <option value={"F"}>F</option>
      </Select>
      <Typography>High Alt:</Typography>
      <Select name="high_alt" defaultValue={"False"} native>
        <option value={"False"}>No</option>
        <option value={"True"}>Yes</option>
      </Select>
    </div>
  );
};

export default AgeGender;
