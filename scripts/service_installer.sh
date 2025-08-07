#!/bin/bash

base_dir=$(dirname "$0")
log_path="$base_dir/../logs/provisioning.log"
provisioning_log(log_path) {
    echo "{\"level\":\"$1\",\"message\":\"$2\",\"ip\":\"$3\",\"timestamp\":\"$(date '+%Y-%m-%dT%H:%M:%S.%6N')\"}" >> "$log_path"
    echo "$2"
}provisioning_log() {
    local level="$1"
    local message="$2"
    local ip="$3"
    echo "{\"level\":\"$level\",\"message\":\"$message\",\"ip\":\"$ip\",\"timestamp\":\"$(date '+%Y-%m-%dT%H:%M:%S.%6N')\"}" >> "$log_path"
    echo "$message"
}  

#define available_services

declare -A services
services=(["docker"]="Installing Docker" ["kubernetes"]="Installing Kubernetes" ["nginx"]="Installing Nginx" ["apache"]="Installing Apache")=true

#service installation loop
for service in "${!services[@]}"; do
    provisioning_log "INFO" "${services[$service]}" "$service"
done

    sleep 5
    provisioning_log "INFO" "$service installed successfully" "$service"
done

    provisioning_log "INFO" "$service installed successfully" "$service"
done
log MESSAGE "Selecting service to install..." "localhost"

    provisioning_log "INFO" "Installing $service on $machine" "$machine"
    sleep 5
    provisioning_log "INFO" "$service installed on $machine" "$machine"
done

esac

#log saccessful installation
provisioning_log "INFO" "$service installed successfully" "$machine"
#!/bin/bash