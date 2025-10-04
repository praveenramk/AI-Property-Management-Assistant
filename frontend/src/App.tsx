import React from 'react';
import { BrowserRouter as Router, Route, Switch } from 'react-router-dom';
import Dashboard from './pages/Dashboard';
import Properties from './pages/Properties';
import Tenants from './pages/Tenants';
import Maintenance from './pages/Maintenance';
import PropertyList from './components/PropertyList';
import TenantList from './components/TenantList';
import MaintenanceForm from './components/MaintenanceForm';
import ChatAssistant from './components/ChatAssistant';

const App = () => {
  return (
    <Router>
      <Switch>
        <Route path="/" exact component={Dashboard} />
        <Route path="/properties" component={Properties} />
        <Route path="/tenants" component={Tenants} />
        <Route path="/maintenance" component={Maintenance} />
      </Switch>
      <PropertyList />
      <TenantList />
      <MaintenanceForm />
      <ChatAssistant />
    </Router>
  );
};

export default App;