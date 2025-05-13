package com.pi.pi_ods3.models;

import com.fasterxml.jackson.annotation.JsonIgnore;

import jakarta.persistence.Column;
import jakarta.persistence.Entity;
import jakarta.persistence.FetchType;
import jakarta.persistence.GeneratedValue;
import jakarta.persistence.GenerationType;
import jakarta.persistence.Id;
import jakarta.persistence.JoinColumn;
import jakarta.persistence.ManyToOne;
import jakarta.persistence.OneToOne;
import jakarta.persistence.Table;
import lombok.AllArgsConstructor;
import lombok.Data;
import lombok.NoArgsConstructor;

@Entity
@Data
@NoArgsConstructor
@AllArgsConstructor
@Table(name = "bula")
public class Bula {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;

    @OneToOne(fetch = FetchType.LAZY)
    @JoinColumn(name = "medicamento_id")
    @JsonIgnore
    private Medicamento medicamento;

    @Column(name = "indicacao", length = 3000)
    private String indicacao;

    @Column(name = "uso", length = 3000)
    private String uso;

    @Column(name = "funcionamento", length = 3000)
    private String funcionamento;

    @Column(name = "nao_usar", length = 3000)
    private String naoUsar;

    @Column(name = "antes_de_usar", length = 4000)
    private String antesDeUsar;

    @Column(name = "males", length = 4000)
    private String males;

    @Column(name = "armazenamento", length = 4000)
    private String armazenamento;

    @Column(name = "esquecer_de_usar", length = 2000)
    private String esquecerDeUsar;

    @Column(name = "superdose", length = 2000)
    private String superdose;

    @Column(name = "apresentacao", length = 4000)
    private String apresentacao;

    @Column(length = 2000)
    private String composicao;

}
