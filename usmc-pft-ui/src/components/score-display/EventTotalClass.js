import React from "react";
import CountUp from "react-countup";
import CancelOutlinedIcon from "@material-ui/icons/CancelOutlined";
import CheckCircleIcon from "@material-ui/icons/CheckCircle";
import ErrorOutlineOutlinedIcon from "@material-ui/icons/ErrorOutlineOutlined";
import ReportProblemOutlinedIcon from "@material-ui/icons/ReportProblemOutlined";
import { Typography } from "@material-ui/core";

import styles from "./ScoreDisplay.module.scss";

const classLookup = {
  1: "1st Class",
  2: "2nd Class",
  3: "3rd Class",
  0: "PFT/CFT Failure",
};

const colorLookup = {
  1: "#388e3c", //Green 1st Class color
  2: "#CCCC00", //Yellow 2nd Class color
  3: "#FF8300", //Orange 3rd Class color
  0: "#FF0000", //Red event failure color
};

const iconLookup = {
  1: <CheckCircleIcon style={{ fontSize: "40px" }} />,
  2: <ErrorOutlineOutlinedIcon style={{ fontSize: "40px" }} />,
  3: <ReportProblemOutlinedIcon style={{ fontSize: "40px" }} />,
  0: <CancelOutlinedIcon style={{ fontSize: "40px" }} />,
};

const EventTotalClass = ({ total: { score, eventClass } }) => {
  const classString = classLookup[eventClass];
  const classColor = colorLookup[eventClass];
  const classIcon = iconLookup[eventClass];

  return (
    <div className={styles.container}>
      <div className={styles.totalScore}>
        <Typography variant="h4">Total:</Typography>
        <Typography variant="h4" style={{ color: classColor }}>
          <CountUp start={0} end={score} duration={1} />
        </Typography>
      </div>
      <div className={styles.container} style={{ color: classColor }}>
        {classIcon}
        <Typography variant="h5">{classString}</Typography>
      </div>
    </div>
  );
};

export default EventTotalClass;
