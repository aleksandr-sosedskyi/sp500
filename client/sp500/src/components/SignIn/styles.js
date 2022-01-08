import { makeStyles } from '@mui/styles';

const useStyles = makeStyles({
  mainContainer: {
    position: 'absolute',
    top: '50%',
    left: '50%',
    transform: 'translate(-50%, -50%)',
    minWidth: '576px',
  },
  submitButton: {
    backgroundColor: 'black !important',
  },
  linkText: {
    color: 'black !important',
  },
  formBox: {
    width: '100%',
  },
});

export default useStyles;
