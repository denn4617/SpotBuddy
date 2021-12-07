import React, { useState } from 'react';
import { Alert, Button, TextInput, View, StyleSheet } from 'react-native';
import axios from 'axios';
import APIKit, {setClientToken} from '../../shared/APIKit';

const Login = () => {
  const [username, setUsername] = useState('')
  const [password, setPassword] = useState('')
  const [errors, setErrors] = useState({});
  const [isAuthorized, setIsAuthorized] = useState(false)
  const [isLoading, setIsLoading] = useState(false) 

  const onSubmitClick = (e) => {
    const onSuccess = ({data}) => {
      console.log("Whoop")
      console.log(data.access_token)
      setClientToken(data.access_token)
      setIsLoading(false)
      setIsAuthorized(true)
    };

    const onFailure = error => {
      console.log(error);
      setErrors({errors: error.response.data});
      setIsLoading(false);
    }

    APIKit.post('http://192.168.0.107:5000/api/login', {
      username: username,
      password: password
    })
    .then(onSuccess)
    .catch(onFailure)
  }

  const styles = StyleSheet.create({
    container: {
      flex: 1,
      alignItems: 'center',
      justifyContent: 'center',
    },
    input: {
      width: 200,
      height: 44,
      padding: 10,
      borderWidth: 1,
      borderColor: 'green',
      borderRadius: 20,
      marginBottom: 10,
    },
  });

  return (
    <View style={styles.container}>
      <TextInput
        value={username}
        onChangeText={(username) => setUsername({ username })}
        placeholder={'Username'}
        style={styles.input}
      />
      <TextInput
        value={password}
        onChangeText={(password) => setPassword({ password })}
        placeholder={'Password'}
        secureTextEntry={true}
        style={styles.input}
      />
      
      <Button
        title={'Login'}
        style={styles.input}
        onPress={() => onSubmitClick()}
      />
    </View>
  );
}

export default Login


// export default class App extends Component {
//   constructor(props) {
//     super(props);
    
//     const [username, setUsername] = useState('')
//     const [password, setPassword] = useState('')
//   }
  
//   onLogin() {
//     const { username, password } = this.state;

//     Alert.alert('Credentials', `${username} + ${password}`);
//   }

//   render() {
//     return (
//       <View style={styles.container}>
//         <TextInput
//           value={this.state.username}
//           onChangeText={(username) => this.setState({ username })}
//           placeholder={'Username'}
//           style={styles.input}
//         />
//         <TextInput
//           value={this.state.password}
//           onChangeText={(password) => this.setState({ password })}
//           placeholder={'Password'}
//           secureTextEntry={true}
//           style={styles.input}
//         />
        
//         <Button
//           title={'Login'}
//           style={styles.input}
//           onPress={this.onLogin.bind(this)}
//         />
//       </View>
//     );
//   }
// }

// const styles = StyleSheet.create({
//   container: {
//     flex: 1,
//     alignItems: 'center',
//     justifyContent: 'center',
//   },
//   input: {
//     width: 200,
//     height: 44,
//     padding: 10,
//     borderWidth: 1,
//     borderColor: 'green',
//     borderRadius: 20,
//     marginBottom: 10,
//   },
// });