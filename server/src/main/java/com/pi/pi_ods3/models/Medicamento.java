package com.pi.pi_ods3.models;

import java.util.List;
import java.util.Map;

import org.springframework.data.mongodb.core.mapping.Document;

import jakarta.persistence.CollectionTable;
import jakarta.persistence.Column;
import jakarta.persistence.ElementCollection;
import jakarta.persistence.Embeddable;
import jakarta.persistence.Embedded;
import jakarta.persistence.Entity;
import jakarta.persistence.FetchType;
import jakarta.persistence.GeneratedValue;
import jakarta.persistence.GenerationType;
import jakarta.persistence.Id;
import jakarta.persistence.JoinColumn;
import jakarta.persistence.MapKeyColumn;
import jakarta.persistence.OneToMany;
import jakarta.persistence.OneToOne;
import jakarta.persistence.Table;
import lombok.AllArgsConstructor;
import lombok.Data;
import lombok.Getter;
import lombok.NoArgsConstructor;
import lombok.Setter;

// @Entity
@Data
// @NoArgsConstructor
// @AllArgsConstructor
// @Table(name = "medicamento")
@Document(collection = "medicamento")
public class Medicamento {
    @Id
    // @GeneratedValue(strategy = GenerationType.IDENTITY)
    private String id;

    private String nome;
    
    // @Column(name = "principio_ativo")
    private String principioAtivo;

    // @OneToOne(mappedBy = "medicamento", fetch = FetchType.LAZY)
    private Bula bula;
        
}