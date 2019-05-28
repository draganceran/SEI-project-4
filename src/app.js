import React from 'react'
import ReactDOM from 'react-dom'
import axios from 'axios'

class App extends React.Component {

  componentDidMount() {
    axios.get('/api/farms')
      .then(res => this.setState({ farms: res.data }))
  }

  render() {
    if(!this.state) return <p>Loading...</p>
    return (
      <div>
        {this.state.farms.map(farm => <div key={farm.id}>
          <h2>{farm.name}</h2>
          <p>{farm.address}</p>
          <p>{farm.description}</p>
          <p>{farm.image}</p>
        </div>)}
      </div>
    )
  }
}

ReactDOM.render(
  <App />,
  document.getElementById('root')
)
