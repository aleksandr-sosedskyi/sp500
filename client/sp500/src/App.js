import { Grid } from '@mui/material';
import { Typography } from '@mui/material';
import { BrowserRouter, Routes, Route } from 'react-router-dom';
import SignIn from './components/SignIn';
import SignUp from './components/SignUp';
import ForgotPassword from './components/ForgotPassword';
import useStyles from './styles';

function App() {
  const classes = useStyles();

  return (
    <>
      <Grid container>
        <Grid item className={classes.header} xs={12}>
          <Typography className={classes.headerTitle} variant="h5">
            Investment Tools
          </Typography>
        </Grid>
      </Grid>
      <BrowserRouter>
        <Routes>
          <Route path="/signin" element={<SignIn />} />
          <Route path="/signup" element={<SignUp />} />
          <Route path="/forgot-password" element={<ForgotPassword />} />
        </Routes>
      </BrowserRouter>
    </>
  );
}

export default App;
